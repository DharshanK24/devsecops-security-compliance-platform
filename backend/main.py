from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.app.database.connection import engine

from backend.app.models.user import User
from backend.app.models.scan_result import ScanResult
from backend.app.models.compliance_result import ComplianceResult

from backend.app.api.user import router as user_router
from backend.app.api.dashboard import router as dashboard_router
from backend.app.api.scanner import router as scanner_router
from backend.app.api.compliance import router as compliance_router
from backend.app.api.reports import router as reports_router


app = FastAPI(
    title="DevSecOps Security & Compliance Platform",
    version="1.0.0"
)


# ==========================================
# CREATE DATABASE TABLES
# ==========================================

User.metadata.create_all(bind=engine)
ScanResult.metadata.create_all(bind=engine)
ComplianceResult.metadata.create_all(bind=engine)


# ==========================================
# CORS CONFIGURATION
# ==========================================
# Allow only the local frontend.
# Do NOT use allow_origins=["*"] in production.

ALLOWED_ORIGINS = [
    "http://127.0.0.1:5500",
    "http://localhost:5500",
]


app.add_middleware(
    CORSMiddleware,

    allow_origins=ALLOWED_ORIGINS,

    allow_credentials=False,

    allow_methods=[
        "GET",
        "POST",
        "PUT",
        "DELETE",
        "OPTIONS",
    ],

    allow_headers=[
        "Authorization",
        "Content-Type",
        "Accept",
    ],
)


# ==========================================
# API ROUTES
# ==========================================

app.include_router(user_router)
app.include_router(dashboard_router)
app.include_router(scanner_router)
app.include_router(compliance_router)
app.include_router(reports_router)


# ==========================================
# HOME
# ==========================================

@app.get("/")
def home():
    return {
        "message": "Welcome to DevSecOps Security & Compliance Platform"
    }


# ==========================================
# HEALTH CHECK
# ==========================================

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }