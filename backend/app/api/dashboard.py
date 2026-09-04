from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session

from backend.app.core.security import verify_token
from backend.app.database.connection import get_db
from backend.app.models.scan_result import ScanResult
from backend.app.models.compliance_result import ComplianceResult


router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)

security = HTTPBearer()


@router.get("/")
def dashboard(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):
    # Get JWT token
    token = credentials.credentials

    # Verify token
    payload = verify_token(token)

    if not payload:
        return {
            "message": "Invalid or expired token"
        }

    # Get logged-in user ID
    user_id = int(payload.get("sub"))

    # -----------------------------------
    # Latest Security Scan
    # -----------------------------------

    latest_scan = (
        db.query(ScanResult)
        .filter(ScanResult.user_id == user_id)
        .order_by(ScanResult.id.desc())
        .first()
    )

    if latest_scan:

        security_data = {
            "security_score": latest_scan.security_score,
            "vulnerabilities": (
                latest_scan.critical
                + latest_scan.high
                + latest_scan.medium
                + latest_scan.low
            ),
            "critical": latest_scan.critical,
            "high": latest_scan.high,
            "medium": latest_scan.medium,
            "low": latest_scan.low
        }

        scan_data = {
            "scan_id": latest_scan.id,
            "total_checks": latest_scan.total_checks,
            "passed_checks": latest_scan.passed_checks
        }

    else:

        security_data = {
            "security_score": 0,
            "vulnerabilities": 0,
            "critical": 0,
            "high": 0,
            "medium": 0,
            "low": 0
        }

        scan_data = {
            "scan_id": None,
            "total_checks": 0,
            "passed_checks": 0
        }

    # -----------------------------------
    # Latest Compliance Scan
    # -----------------------------------

    latest_compliance = (
        db.query(ComplianceResult)
        .filter(ComplianceResult.user_id == user_id)
        .order_by(ComplianceResult.id.desc())
        .first()
    )

    if latest_compliance:

        compliance_data = {
            "scan_id": latest_compliance.id,
            "status": latest_compliance.status,
            "compliance_score": latest_compliance.compliance_score,
            "total_checks": latest_compliance.total_checks,
            "compliant_checks": latest_compliance.compliant_checks,
            "review_required": latest_compliance.review_required
        }

    else:

        compliance_data = {
            "scan_id": None,
            "status": "Not Scanned",
            "compliance_score": 0,
            "total_checks": 0,
            "compliant_checks": 0,
            "review_required": 0
        }

    # -----------------------------------
    # Dashboard Response
    # -----------------------------------

    return {
        "message": "Dashboard data loaded successfully",

        "user": {
            "id": payload.get("sub"),
            "username": payload.get("username"),
            "email": payload.get("email")
        },

        "security": security_data,

        "scan": scan_data,

        "compliance": compliance_data
    }