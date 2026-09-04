from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from backend.app.core.security import verify_token
from backend.app.database.connection import get_db
from backend.app.models.scan_result import ScanResult
from backend.app.models.compliance_result import ComplianceResult
from backend.app.services.pdf_report import generate_combined_report

import os


# ==========================================
# ROUTER
# ==========================================

router = APIRouter(
    prefix="/reports",
    tags=["Reports"]
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
# SECURITY REPORT
# ==========================================

@router.get("/security")
def security_report(
    payload=Depends(get_current_user),
    db: Session = Depends(get_db)
):

    user_id = int(payload.get("sub"))

    latest_scan = (
        db.query(ScanResult)
        .filter(
            ScanResult.user_id == user_id
        )
        .order_by(
            ScanResult.id.desc()
        )
        .first()
    )

    if not latest_scan:
        return {
            "message": "No security scan found",

            "user": {
                "id": payload.get("sub"),
                "username": payload.get("username"),
                "email": payload.get("email")
            }
        }

    critical = latest_scan.critical or 0
    high = latest_scan.high or 0
    medium = latest_scan.medium or 0
    low = latest_scan.low or 0

    total_vulnerabilities = (
        critical +
        high +
        medium +
        low
    )

    total_checks = latest_scan.total_checks or 0
    passed_checks = latest_scan.passed_checks or 0

    return {
        "message": "Security report loaded successfully",

        "user": {
            "id": payload.get("sub"),
            "username": payload.get("username"),
            "email": payload.get("email")
        },

        "scan_id": latest_scan.id,

        "security_score": latest_scan.security_score,

        "total_checks": total_checks,

        "passed_checks": passed_checks,

        "failed_checks": (
            total_checks -
            passed_checks
        ),

        "findings": {
            "critical": critical,
            "high": high,
            "medium": medium,
            "low": low
        },

        "summary": {
            "total_vulnerabilities":
                total_vulnerabilities
        },

        "created_at":
            latest_scan.created_at
    }


# ==========================================
# COMPLIANCE REPORT
# ==========================================

@router.get("/compliance")
def compliance_report(
    payload=Depends(get_current_user),
    db: Session = Depends(get_db)
):

    user_id = int(payload.get("sub"))

    latest_compliance = (
        db.query(ComplianceResult)
        .filter(
            ComplianceResult.user_id == user_id
        )
        .order_by(
            ComplianceResult.id.desc()
        )
        .first()
    )

    if not latest_compliance:
        return {
            "message": "No compliance scan found",

            "user": {
                "id": payload.get("sub"),
                "username": payload.get("username"),
                "email": payload.get("email")
            }
        }

    return {
        "message":
            "Compliance report loaded successfully",

        "user": {
            "id": payload.get("sub"),
            "username": payload.get("username"),
            "email": payload.get("email")
        },

        "scan_id":
            latest_compliance.id,

        "compliance_score":
            latest_compliance.compliance_score,

        "total_checks":
            latest_compliance.total_checks,

        "compliant_checks":
            latest_compliance.compliant_checks,

        "review_required":
            latest_compliance.review_required,

        "status":
            latest_compliance.status,

        "created_at":
            latest_compliance.created_at
    }


# ==========================================
# COMBINED REPORT
# ==========================================

@router.get("/summary")
def combined_report(
    payload=Depends(get_current_user),
    db: Session = Depends(get_db)
):

    user_id = int(payload.get("sub"))

    # ======================================
    # LATEST SECURITY
    # ======================================

    latest_security = (
        db.query(ScanResult)
        .filter(
            ScanResult.user_id == user_id
        )
        .order_by(
            ScanResult.id.desc()
        )
        .first()
    )

    # ======================================
    # LATEST COMPLIANCE
    # ======================================

    latest_compliance = (
        db.query(ComplianceResult)
        .filter(
            ComplianceResult.user_id == user_id
        )
        .order_by(
            ComplianceResult.id.desc()
        )
        .first()
    )

    # ======================================
    # SECURITY VALUES
    # ======================================

    if latest_security:

        critical = latest_security.critical or 0
        high = latest_security.high or 0
        medium = latest_security.medium or 0
        low = latest_security.low or 0

        security_vulnerabilities = (
            critical +
            high +
            medium +
            low
        )

        security_total_checks = (
            latest_security.total_checks or 0
        )

        security_passed_checks = (
            latest_security.passed_checks or 0
        )

    else:

        critical = 0
        high = 0
        medium = 0
        low = 0

        security_vulnerabilities = 0
        security_total_checks = 0
        security_passed_checks = 0

    # ======================================
    # COMBINED RESPONSE
    # ======================================

    return {

        "message":
            "DevSecOps security and compliance report",

        "user": {

            "id":
                payload.get("sub"),

            "username":
                payload.get("username"),

            "email":
                payload.get("email")

        },

        "security": {

            "scan_id":
                latest_security.id
                if latest_security
                else None,

            "security_score":
                latest_security.security_score
                if latest_security
                else 0,

            "total_checks":
                security_total_checks,

            "passed_checks":
                security_passed_checks,

            "failed_checks":
                (
                    security_total_checks -
                    security_passed_checks
                ),

            "vulnerabilities":
                security_vulnerabilities,

            "findings": {

                "critical":
                    critical,

                "high":
                    high,

                "medium":
                    medium,

                "low":
                    low
            },

            "created_at":
                latest_security.created_at
                if latest_security
                else None
        },

        "compliance": {

            "scan_id":
                latest_compliance.id
                if latest_compliance
                else None,

            "compliance_score":
                latest_compliance.compliance_score
                if latest_compliance
                else 0,

            "total_checks":
                latest_compliance.total_checks
                if latest_compliance
                else 0,

            "compliant_checks":
                latest_compliance.compliant_checks
                if latest_compliance
                else 0,

            "review_required":
                latest_compliance.review_required
                if latest_compliance
                else 0,

            "status":
                latest_compliance.status
                if latest_compliance
                else "No Scan",

            "created_at":
                latest_compliance.created_at
                if latest_compliance
                else None
        }
    }


# ==========================================
# PDF COMBINED REPORT
# ==========================================

@router.get("/pdf")
def download_pdf_report(
    payload=Depends(get_current_user),
    db: Session = Depends(get_db)
):

    user_id = int(payload.get("sub"))

    username = payload.get(
        "username",
        "User"
    )

    email = payload.get(
        "email",
        "-"
    )

    # ======================================
    # LATEST SECURITY SCAN
    # ======================================

    latest_security = (
        db.query(ScanResult)
        .filter(
            ScanResult.user_id == user_id
        )
        .order_by(
            ScanResult.id.desc()
        )
        .first()
    )

    # ======================================
    # LATEST COMPLIANCE SCAN
    # ======================================

    latest_compliance = (
        db.query(ComplianceResult)
        .filter(
            ComplianceResult.user_id == user_id
        )
        .order_by(
            ComplianceResult.id.desc()
        )
        .first()
    )

    # ======================================
    # SECURITY DATA
    # ======================================

    if latest_security:

        critical = latest_security.critical or 0
        high = latest_security.high or 0
        medium = latest_security.medium or 0
        low = latest_security.low or 0

        total_checks = (
            latest_security.total_checks or 0
        )

        passed_checks = (
            latest_security.passed_checks or 0
        )

        total_vulnerabilities = (
            critical +
            high +
            medium +
            low
        )

        security_data = {

            "scan_id":
                latest_security.id,

            "security_score":
                latest_security.security_score,

            "total_checks":
                total_checks,

            "passed_checks":
                passed_checks,

            "failed_checks":
                total_checks -
                passed_checks,

            "findings": {

                "critical":
                    critical,

                "high":
                    high,

                "medium":
                    medium,

                "low":
                    low
            },

            "summary": {

                "total_vulnerabilities":
                    total_vulnerabilities
            },

            "created_at":
                latest_security.created_at
        }

    else:

        security_data = {

            "scan_id": None,

            "security_score": 0,

            "total_checks": 0,

            "passed_checks": 0,

            "failed_checks": 0,

            "findings": {

                "critical": 0,

                "high": 0,

                "medium": 0,

                "low": 0
            },

            "summary": {

                "total_vulnerabilities": 0
            },

            "created_at": None
        }

    # ======================================
    # COMPLIANCE DATA
    # ======================================

    if latest_compliance:

        compliance_data = {

            "scan_id":
                latest_compliance.id,

            "compliance_score":
                latest_compliance.compliance_score,

            "total_checks":
                latest_compliance.total_checks,

            "compliant_checks":
                latest_compliance.compliant_checks,

            "review_required":
                latest_compliance.review_required,

            "status":
                latest_compliance.status,

            "created_at":
                latest_compliance.created_at
        }

    else:

        compliance_data = {

            "scan_id": None,

            "compliance_score": 0,

            "total_checks": 0,

            "compliant_checks": 0,

            "review_required": 0,

            "status": "No Scan",

            "created_at": None
        }

    # ======================================
    # REPORT DIRECTORY
    # ======================================

    report_directory = "reports"

    os.makedirs(
        report_directory,
        exist_ok=True
    )

    # ======================================
    # PDF FILE PATH
    # ======================================

    pdf_path = os.path.join(
        report_directory,
        f"devsecops_report_{user_id}.pdf"
    )

    # ======================================
    # GENERATE PDF
    # ======================================

    try:

        generate_combined_report(

            filepath=pdf_path,

            username=username,

            email=email,

            security_data=security_data,

            compliance_data=compliance_data
        )

    except Exception as error:

        print(
            "PDF Generation Error:",
            error
        )

        raise HTTPException(
            status_code=500,
            detail="Unable to generate PDF report"
        )

    # ======================================
    # CHECK PDF
    # ======================================

    if not os.path.exists(pdf_path):

        raise HTTPException(
            status_code=500,
            detail="PDF report generation failed"
        )

    # ======================================
    # RETURN PDF
    # ======================================

    return FileResponse(

        path=pdf_path,

        media_type="application/pdf",

        filename="DevSecOps_Report.pdf"
    )