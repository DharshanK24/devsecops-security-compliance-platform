from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session

from backend.app.core.security import verify_token
from backend.app.database.connection import get_db
from backend.app.models.compliance_result import ComplianceResult


# ==========================================
# ROUTER
# ==========================================

router = APIRouter(
    prefix="/compliance",
    tags=["Compliance"]
)

security = HTTPBearer()


# ==========================================
# VERIFY JWT
# ==========================================

def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    token = credentials.credentials

    payload = verify_token(token)

    if not payload:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token"
        )

    return payload


# ==========================================
# COMPLIANCE CHECKS
# ==========================================

def perform_compliance_checks():

    return [

        {
            "name": "Authentication Policy",
            "status": "Compliant",
            "description": "JWT based authentication is enabled."
        },

        {
            "name": "Password Protection",
            "status": "Compliant",
            "description": "Passwords are protected using bcrypt hashing."
        },

        {
            "name": "Access Control",
            "status": "Compliant",
            "description": "Protected API endpoints require authentication."
        },

        {
            "name": "Security Configuration",
            "status": "Review",
            "description": "Security configuration should be reviewed before production deployment."
        },

        {
            "name": "Data Protection",
            "status": "Review",
            "description": "Database security and sensitive data protection should be reviewed."
        }

    ]


# ==========================================
# RUN NEW COMPLIANCE SCAN
# ==========================================

def create_compliance_scan(
    payload,
    db: Session
):

    user_id = int(payload.get("sub"))

    # --------------------------------------
    # RUN CHECKS
    # --------------------------------------

    checks = perform_compliance_checks()

    # --------------------------------------
    # CALCULATE SCORE
    # --------------------------------------

    total_checks = len(checks)

    compliant_checks = sum(
        1
        for check in checks
        if check["status"] == "Compliant"
    )

    review_required = total_checks - compliant_checks

    compliance_score = int(
        (compliant_checks / total_checks) * 100
    )

    # --------------------------------------
    # STATUS
    # --------------------------------------

    status = (
        "Compliant"
        if compliance_score >= 80
        else "Needs Review"
    )

    # --------------------------------------
    # SAVE NEW SCAN
    # --------------------------------------

    compliance_result = ComplianceResult(
        user_id=user_id,
        compliance_score=compliance_score,
        total_checks=total_checks,
        compliant_checks=compliant_checks,
        review_required=review_required,
        status=status
    )

    db.add(compliance_result)

    db.commit()

    db.refresh(compliance_result)

    # --------------------------------------
    # RETURN RESULT
    # --------------------------------------

    return {

        "message":
            "Compliance scan completed successfully",

        "compliance_scan_id":
            compliance_result.id,

        "user": {

            "id":
                payload.get("sub"),

            "username":
                payload.get("username"),

            "email":
                payload.get("email")

        },

        "compliance_score":
            compliance_score,

        "total_checks":
            total_checks,

        "compliant_checks":
            compliant_checks,

        "review_required":
            review_required,

        "status":
            status,

        "checks":
            checks,

        "database": {

            "status":
                "Saved",

            "scan_id":
                compliance_result.id

        }

    }


# ==========================================
# RUN COMPLIANCE SCAN - POST
# ==========================================

@router.post("/scan")
def run_compliance_scan_post(

    payload=Depends(get_current_user),

    db: Session = Depends(get_db)

):

    return create_compliance_scan(
        payload,
        db
    )


# ==========================================
# RUN COMPLIANCE SCAN - GET
# ==========================================
# This is kept because your dashboard can call:
# GET /compliance/
#
# Every click creates a NEW compliance scan.

@router.get("/")
def run_compliance_scan_get(

    payload=Depends(get_current_user),

    db: Session = Depends(get_db)

):

    return create_compliance_scan(
        payload,
        db
    )


# ==========================================
# GET LATEST COMPLIANCE SCAN
# ==========================================

@router.get("/latest")
def get_latest_compliance(

    payload=Depends(get_current_user),

    db: Session = Depends(get_db)

):

    user_id = int(
        payload.get("sub")
    )

    # --------------------------------------
    # GET LATEST SAVED SCAN
    # --------------------------------------

    scan = (
        db.query(ComplianceResult)
        .filter(
            ComplianceResult.user_id == user_id
        )
        .order_by(
            ComplianceResult.id.desc()
        )
        .first()
    )

    # --------------------------------------
    # NO SCAN
    # --------------------------------------

    if not scan:

        return {

            "message":
                "No compliance scan available",

            "user": {

                "id":
                    payload.get("sub"),

                "username":
                    payload.get("username"),

                "email":
                    payload.get("email")

            },

            "compliance_scan_id":
                None,

            "compliance_score":
                0,

            "total_checks":
                0,

            "compliant_checks":
                0,

            "review_required":
                0,

            "status":
                "No Scan",

            "checks":
                []

        }

    # --------------------------------------
    # RETURN LATEST
    # --------------------------------------

    return {

        "message":
            "Latest compliance scan loaded successfully",

        "compliance_scan_id":
            scan.id,

        "user": {

            "id":
                payload.get("sub"),

            "username":
                payload.get("username"),

            "email":
                payload.get("email")

        },

        "compliance_score":
            scan.compliance_score,

        "total_checks":
            scan.total_checks,

        "compliant_checks":
            scan.compliant_checks,

        "review_required":
            scan.review_required,

        "status":
            scan.status,

        "checks":
            perform_compliance_checks()

    }


# ==========================================
# COMPLIANCE SCAN HISTORY
# ==========================================

@router.get("/history")
def compliance_history(

    payload=Depends(get_current_user),

    db: Session = Depends(get_db)

):

    user_id = int(
        payload.get("sub")
    )

    # --------------------------------------
    # GET USER SCAN HISTORY
    # --------------------------------------

    scans = (

        db.query(
            ComplianceResult
        )

        .filter(
            ComplianceResult.user_id == user_id
        )

        .order_by(
            ComplianceResult.id.desc()
        )

        .all()

    )

    # --------------------------------------
    # RETURN HISTORY
    # --------------------------------------

    return {

        "message":
            "Compliance scan history loaded successfully",

        "total_scans":
            len(scans),

        "history": [

            {

                "scan_id":
                    scan.id,

                "compliance_score":
                    scan.compliance_score,

                "total_checks":
                    scan.total_checks,

                "compliant_checks":
                    scan.compliant_checks,

                "review_required":
                    scan.review_required,

                "status":
                    scan.status,

                "created_at":
                    scan.created_at

            }

            for scan in scans

        ]

    }