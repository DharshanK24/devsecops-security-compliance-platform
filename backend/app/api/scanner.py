from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session

from backend.app.core.security import verify_token
from backend.app.database.connection import get_db
from backend.app.models.scan_result import ScanResult

from backend.app.services.security_scanner import (
    scan_project,
    calculate_security_score,
    get_security_summary
)


# ==========================================
# ROUTER
# ==========================================

router = APIRouter(
    prefix="/scanner",
    tags=["Security Scanner"]
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
# GET LATEST SECURITY SCAN
# ==========================================

@router.get("/")
def get_latest_scan(
    payload=Depends(get_current_user),
    db: Session = Depends(get_db)
):

    user_id = int(payload.get("sub"))

    scan = (
        db.query(ScanResult)
        .filter(
            ScanResult.user_id == user_id
        )
        .order_by(
            ScanResult.id.desc()
        )
        .first()
    )

    # ------------------------------------------
    # NO PREVIOUS SCAN
    # ------------------------------------------

    if not scan:

        return {
            "message": "No security scan available",

            "user": {
                "id": payload.get("sub"),
                "username": payload.get("username"),
                "email": payload.get("email")
            },

            "security_score": 0,
            "total_checks": 0,
            "passed_checks": 0,
            "vulnerabilities": 0,

            "summary": {
                "critical": 0,
                "high": 0,
                "medium": 0,
                "low": 0
            },

            "findings": []
        }

    # ------------------------------------------
    # GET CURRENT PROJECT FINDINGS
    # WITHOUT SAVING A NEW SCAN
    # ------------------------------------------

    findings = scan_project(".")

    # ------------------------------------------
    # RETURN LATEST SAVED RESULT
    # ------------------------------------------

    return {

        "message":
            "Latest security scan loaded successfully",

        "scan_id":
            scan.id,

        "user": {

            "id":
                payload.get("sub"),

            "username":
                payload.get("username"),

            "email":
                payload.get("email")

        },

        "security_score":
            scan.security_score,

        "total_checks":
            scan.total_checks,

        "passed_checks":
            scan.passed_checks,

        "vulnerabilities":
            (
                scan.critical
                + scan.high
                + scan.medium
                + scan.low
            ),

        "summary": {

            "critical":
                scan.critical,

            "high":
                scan.high,

            "medium":
                scan.medium,

            "low":
                scan.low

        },

        "findings":
            findings

    }


# ==========================================
# RUN NEW SECURITY SCAN
# ==========================================

@router.post("/scan")
def run_security_scan(
    payload=Depends(get_current_user),
    db: Session = Depends(get_db)
):

    # ======================================
    # USER ID
    # ======================================

    user_id = int(
        payload.get("sub")
    )


    # ======================================
    # RUN ACTUAL PROJECT SCANNER
    # ======================================

    findings = scan_project(".")


    # ======================================
    # CALCULATE SECURITY SCORE
    # ======================================

    security_score = calculate_security_score(
        findings
    )


    # ======================================
    # SECURITY SUMMARY
    # ======================================

    summary = get_security_summary(
        findings
    )


    # ======================================
    # CHECK COUNTS
    # ======================================

    total_checks = len(findings)

    passed_checks = sum(
        1
        for finding in findings
        if finding.get("status") == "Passed"
    )


    # ======================================
    # SAVE RESULT
    # ======================================

    scan_result = ScanResult(

        user_id=user_id,

        security_score=security_score,

        total_checks=total_checks,

        passed_checks=passed_checks,

        critical=summary.get("critical", 0),

        high=summary.get("high", 0),

        medium=summary.get("medium", 0),

        low=summary.get("low", 0)

    )


    db.add(scan_result)

    db.commit()

    db.refresh(scan_result)


    # ======================================
    # RETURN NEW SCAN RESULT
    # ======================================

    return {

        "message":
            "Security scan completed successfully",

        "scan_id":
            scan_result.id,

        "user": {

            "id":
                payload.get("sub"),

            "username":
                payload.get("username"),

            "email":
                payload.get("email")

        },

        "security_score":
            security_score,

        "total_checks":
            total_checks,

        "passed_checks":
            passed_checks,

        "vulnerabilities":
            (
                summary.get("critical", 0)
                + summary.get("high", 0)
                + summary.get("medium", 0)
                + summary.get("low", 0)
            ),

        "summary":
            summary,

        "findings":
            findings,

        "database": {

            "status":
                "Saved",

            "scan_id":
                scan_result.id

        }

    }


# ==========================================
# SECURITY SCAN HISTORY
# ==========================================

@router.get("/history")
def scanner_history(

    payload=Depends(get_current_user),

    db: Session = Depends(get_db)

):

    # ======================================
    # USER ID
    # ======================================

    user_id = int(
        payload.get("sub")
    )


    # ======================================
    # GET USER SCANS
    # ======================================

    scans = (

        db.query(ScanResult)

        .filter(
            ScanResult.user_id == user_id
        )

        .order_by(
            ScanResult.id.desc()
        )

        .all()

    )


    # ======================================
    # RETURN HISTORY
    # ======================================

    return {

        "message":
            "Security scan history loaded successfully",

        "total_scans":
            len(scans),

        "history": [

            {

                "scan_id":
                    scan.id,

                "security_score":
                    scan.security_score,

                "total_checks":
                    scan.total_checks,

                "passed_checks":
                    scan.passed_checks,

                "critical":
                    scan.critical,

                "high":
                    scan.high,

                "medium":
                    scan.medium,

                "low":
                    scan.low,

                "created_at":
                    scan.created_at

            }

            for scan in scans

        ]

    }