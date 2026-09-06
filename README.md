# 🛡️ DevSecOps Security & Compliance Platform

A containerized DevSecOps platform for automated security scanning, compliance assessment, monitoring, authentication, CI/CD, and secure application delivery.

---

## 🚀 Project Overview

The DevSecOps Security & Compliance Platform integrates security and compliance checks into a software development workflow.

### Key Features

- JWT-based authentication
- User registration and login
- Security vulnerability scanning
- Security score calculation
- Compliance assessment
- Security and compliance scan history
- Security and compliance reports
- PDF report generation
- Docker containerization
- Nginx reverse proxy
- Prometheus monitoring
- Grafana dashboard
- GitHub Actions CI/CD
- Automated Bandit security scanning

---

## 🎯 Project Objectives

- Automate application security checks
- Detect common security vulnerabilities and misconfigurations
- Provide security and compliance scores
- Maintain security and compliance scan history
- Generate security reports
- Integrate security into the CI/CD workflow
- Containerize application services using Docker
- Monitor application performance and infrastructure

---

## 🏗️ System Architecture

```text
                    ┌──────────────────┐
                    │     Frontend     │
                    │   HTML/CSS/JS    │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │      Nginx       │
                    │  Reverse Proxy   │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │  FastAPI Backend │
                    │     Python       │
                    │    REST APIs     │
                    └──────┬─────┬─────┘
                           │     │
                  ┌────────┘     └──────────┐
                  ▼                         ▼
          ┌────────────────┐       ┌──────────────────┐
          │   PostgreSQL   │       │ Security Scanner │
          │    Database    │       │   & Compliance   │
          └────────────────┘       └──────────────────┘

                         Monitoring
                             │
                     ┌───────┴───────┐
                     ▼               ▼
               ┌───────────┐   ┌───────────┐
               │ Prometheus│──►│  Grafana  │
               │  Metrics  │   │ Dashboard │
               └───────────┘   └───────────┘

                           CI/CD
                             │
                             ▼
                    ┌─────────────────┐
                    │ GitHub Actions  │
                    │ + Bandit Scan   │
                    └─────────────────┘
```

---

## 🛠️ Technology Used

### Frontend

- HTML5
- CSS3
- JavaScript

### Backend

- Python
- FastAPI
- SQLAlchemy

### Database

- PostgreSQL

### Authentication & Security

- JWT Authentication
- bcrypt
- HTTP Bearer Authentication
- Bandit
- Security Scanner
- Compliance Scanner

### DevOps & CI/CD

- Docker
- Docker Compose
- Nginx
- Git
- GitHub
- GitHub Actions

### Monitoring

- Prometheus
- Grafana

### Reporting

- ReportLab
- PDF Reports

### Development Environment

- Windows
- PowerShell
- Visual Studio Code

---

## 📂 Project Structure

```text
DevSecOps Security & Compliance Platform/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── user.py
│   │   │   ├── scanner.py
│   │   │   └── compliance.py
│   │   │
│   │   ├── core/
│   │   │   └── security.py
│   │   │
│   │   ├── database/
│   │   │   ├── connection.py
│   │   │   └── base.py
│   │   │
│   │   ├── models/
│   │   │   ├── user.py
│   │   │   ├── scan_result.py
│   │   │   └── compliance_result.py
│   │   │
│   │   ├── schemas/
│   │   │   └── user.py
│   │   │
│   │   └── services/
│   │       └── security_scanner.py
│   │
│   ├── main.py
│   └── requirements.txt
│
├── frontend/
│   ├── css/
│   ├── js/
│   ├── images/
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   └── dashboard.html
│
├── nginx/
│   └── nginx.conf
│
├── reports/
├── screenshots/
│
├── .github/
│   └── workflows/
│       └── ci-cd.yml
│
├── Dockerfile
├── compose.yaml
├── prometheus.yaml
└── README.md
```

---

## 🔐 Security Features

### JWT Authentication

Users can register and login using JWT-based authentication.

Protected APIs require a valid authentication token.

### Security Scanner

The platform performs security assessment and reports detected vulnerabilities and security misconfigurations.

Security checks include:

- Hardcoded passwords
- API keys
- Secrets
- Access tokens
- Debug configuration
- Permissive CORS configuration

### Compliance Scanner

The platform evaluates configured compliance checks and identifies items that require review.

### Automated Bandit Scan

GitHub Actions runs Bandit automatically during the CI/CD pipeline to identify potential Python security issues.

---

## 📊 Monitoring

Prometheus collects backend application and infrastructure metrics.

Grafana visualizes these metrics through the DevSecOps Monitoring Dashboard.

### Monitoring Metrics

- HTTP Requests
- Request Duration
- CPU Usage
- Memory Usage
- Request Rate
- Service Uptime
- Error Rate
- Python Process Metrics

---

## 🔄 CI/CD Pipeline

GitHub Actions automatically performs:

1. Checkout source code
2. Setup Python
3. Install dependencies
4. Run Bandit security scan
5. Python syntax check
6. Build Docker image
7. Start PostgreSQL
8. Start backend
9. Backend health check
10. Display backend logs if the build fails

### CI/CD Workflow

```text
Developer
    │
    ▼
GitHub Repository
    │
    ▼
GitHub Actions
    │
    ├── Install Dependencies
    ├── Bandit Security Scan
    ├── Syntax Check
    ├── Docker Build
    ├── PostgreSQL
    └── Backend Health Check
```

---

## 🐳 Docker Services

The application uses Docker containers for:

- FastAPI Backend
- PostgreSQL
- Prometheus
- Grafana
- Nginx

### Check Running Containers

```bash
docker ps
```

### Start Services

```bash
docker compose up -d
```

### Stop Services

```bash
docker compose down
```

### View Logs

```bash
docker compose logs
```

---

## ⚙️ Installation & Setup

### Prerequisites

Make sure the following are installed:

- Python 3.x
- PostgreSQL 16+
- Docker Desktop
- Git
- Visual Studio Code

### 1. Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd "DevSecOps Security & Compliance Platform"
```

### 2. Database Setup

Create a PostgreSQL database:

```text
Database Name: devsecops_db
Username: postgres
Port: 5432
```

Update the database connection in:

```text
backend/app/database/connection.py
```

Example:

```python
DATABASE_URL = "postgresql://postgres:<PASSWORD>@localhost:5432/devsecops_db"
```

Replace `<PASSWORD>` with your PostgreSQL password.

> Do not commit actual passwords, API keys, or secrets to GitHub.

### 3. Backend Setup

Create a Python virtual environment:

```bash
python -m venv venv
```

Activate the environment on Windows:

```powershell
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r backend/requirements.txt
```

### 4. Start Backend

```bash
uvicorn backend.main:app --reload
```

Backend:

```text
http://127.0.0.1:8000
```

Swagger API Documentation:

```text
http://127.0.0.1:8000/docs
```

Health Check:

```text
http://127.0.0.1:8000/health
```

Expected response:

```json
{
    "status": "healthy"
}
```

### 5. Frontend Setup

Open a new PowerShell terminal.

Navigate to the frontend directory:

```powershell
cd frontend
```

Start the frontend server:

```bash
python -m http.server 5500
```

Frontend:

```text
http://127.0.0.1:5500
```

### 6. Docker Setup

Check Docker:

```bash
docker --version
```

Check containers:

```bash
docker ps
```

Build services:

```bash
docker compose build
```

Start services:

```bash
docker compose up -d
```

Check status:

```bash
docker ps
```

Stop services:

```bash
docker compose down
```

View logs:

```bash
docker compose logs
```

---

## 🔌 Application Services & Ports

| Service | Port | URL |
|---|---:|---|
| Frontend | 5500 | http://127.0.0.1:5500 |
| FastAPI Backend | 8000 | http://127.0.0.1:8000 |
| PostgreSQL | 5432 | localhost:5432 |
| Nginx | 8080 | http://127.0.0.1:8080 |
| Prometheus | 9090 | http://127.0.0.1:9090 |
| Grafana | 3000 | http://127.0.0.1:3000 |

---

## 🌐 API Endpoints

### Users

```text
POST /users/register
POST /users/login
GET  /users/me
```

### Security Scanner

```text
GET  /scanner/
POST /scanner/scan
GET  /scanner/history
```

### Compliance

```text
GET /compliance/
GET /compliance/history
```

### Reports

```text
GET /reports/security
GET /reports/compliance
GET /reports/summary
GET /reports/pdf
```

### Monitoring

```text
GET /metrics
GET /health
```

---

## 🛡️ Security Scanning Workflow

```text
User
 │
 ▼
Login
 │
 ▼
JWT Authentication
 │
 ▼
Run Security Scan
 │
 ▼
Source Code Analysis
 │
 ▼
Security Findings
 │
 ▼
Severity Classification
 │
 ▼
Security Score
 │
 ▼
Recommendations
 │
 ▼
Database Storage
```

---

## 📋 Compliance Workflow

```text
Application
     │
     ▼
Compliance Checks
     │
     ▼
Security Controls Evaluation
     │
     ▼
Compliance Score
     │
     ▼
Compliance Status
     │
     ▼
Database Storage
     │
     ▼
Compliance History
```

---

## 📈 Security Scan Results

The security scanner generates:

- Security Score
- Total Checks
- Passed Checks
- Vulnerabilities
- Critical Issues
- High Severity Issues
- Medium Severity Issues
- Low Severity Issues
- Security Recommendations

---

## 📋 Compliance Results

The compliance module generates:

- Compliance Score
- Total Checks
- Compliant Checks
- Review Required
- Compliance Status
- Compliance History

---

## 🧪 Testing

The application can be tested using:

- FastAPI Swagger UI
- Frontend Dashboard
- Authentication APIs
- Security Scanner APIs
- Compliance APIs
- Docker Containers
- GitHub Actions CI/CD
- Prometheus
- Grafana

### Current Test Results

| Component | Status |
|---|---|
| Backend Health Check | ✅ PASS |
| Swagger API | ✅ PASS |
| Nginx Reverse Proxy | ✅ PASS |
| Prometheus Metrics | ✅ PASS |
| Prometheus Target | 🟢 UP |
| Grafana Dashboard | ✅ PASS |
| Docker Services | ✅ RUNNING |
| GitHub Actions CI/CD | ✅ SUCCESS |
| Bandit Security Scan | ✅ SUCCESS |

---

## 📸 Screenshots

Add project screenshots to:

```text
screenshots/
```

Recommended screenshots:

1. Registration Page
2. Login Page
3. Dashboard
4. Security Scan Result
5. Security Findings
6. Compliance Result
7. Docker Containers
8. GitHub Actions CI/CD
9. Prometheus Dashboard
10. Grafana Dashboard

---

## 🎓 Project Domain

```text
DevSecOps
Cloud Computing
Cyber Security
Application Security
CI/CD
Containerization
Compliance
Monitoring
```

---

## 🔮 Future Enhancements

- Cloud deployment
- Advanced vulnerability scanning
- Container image vulnerability scanning
- Role-Based Access Control
- Automated security remediation
- Advanced compliance frameworks
- AI-assisted vulnerability analysis
- Automated security alerting
- Advanced security reporting

---

## 🎯 Project Objective

The main objective of this project is to demonstrate how security, compliance, monitoring, authentication, containerization, and CI/CD can be integrated into a single DevSecOps platform.

---

## 👨‍💻 Author

**Dharshan K**

Computer Science and Engineering

Suguna College of Engineering

Coimbatore, Tamil Nadu, India

### Project

**DevSecOps Security & Compliance Platform**

---

## 📜 Conclusion

The DevSecOps Security & Compliance Platform demonstrates how security can be integrated into the software development and deployment lifecycle.

By combining security scanning, compliance assessment, authentication, Docker, CI/CD, Nginx, Prometheus, and Grafana, the platform provides a foundation for building a secure and automated software delivery process.