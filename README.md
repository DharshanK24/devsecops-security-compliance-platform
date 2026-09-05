# DevSecOps Security & Compliance Platform

A containerized DevSecOps platform for automated security scanning, compliance assessment, monitoring, authentication, and report generation.

<<<<<<< HEAD
## 🚀 Project Overview

The DevSecOps Security & Compliance Platform integrates security and compliance checks into a software development workflow.

### Key Features

- JWT-based authentication
- Security vulnerability scanning
- Compliance assessment
- Scan history
- Security and compliance reports
- PDF report generation
- Docker containerization
- Nginx reverse proxy
- Prometheus monitoring
- Grafana dashboard
- GitHub Actions CI/CD
- Automated Bandit security scanning

## 🏗️ Architecture

#text
                    ┌──────────────────┐
                    │     Frontend     │
                    │    HTML/CSS/JS   │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │      Nginx       │
                    │   Reverse Proxy  │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │  FastAPI Backend │
                    │      Python      │
                    └──────┬─────┬─────┘
                           │     │
                ┌──────────┘     └──────────┐
                ▼                           ▼
       ┌────────────────┐          ┌────────────────┐
       │   PostgreSQL   │          │ Security Scan  │
       │    Database    │          │ & Compliance   │
       └────────────────┘          └────────────────┘

                    Monitoring
                         │
              ┌──────────┴──────────┐
              ▼                     ▼
       ┌──────────────┐      ┌──────────────┐
       │  Prometheus  │ ───► │   Grafana    │
       │    Metrics   │      │  Dashboard   │
       └──────────────┘      └──────────────┘

                     CI/CD
                       │
                       ▼
              ┌────────────────┐
              │ GitHub Actions │
              │ + Bandit Scan  │
              └────────────────┘

## 🛠️ Technology Stack

### Backend
- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- JWT Authentication

### Frontend
- HTML
- CSS
- JavaScript

### Security
- Bandit
- Security Scanner
- Compliance Scanner
- JWT Authentication

### DevOps
- Docker
- Docker Compose
- Nginx
- GitHub Actions

### Monitoring
- Prometheus
- Grafana

### Reporting
- ReportLab
- PDF Reports

📂 Project Structure

DevSecOps Security & Compliance Platform/
=======


\## 🚀 Project Overview



The DevSecOps Security \& Compliance Platform integrates security and compliance checks into a software development workflow.



\### Key Features



\- JWT-based authentication

\- Security vulnerability scanning

\- Compliance assessment

\- Scan history

\- Security and compliance reports

\- PDF report generation

\- Docker containerization

\- Nginx reverse proxy

\- Prometheus monitoring

\- Grafana dashboard

\- GitHub Actions CI/CD

\- Automated Bandit security scanning



\## 🏗️ Architecture



&#x20;                        ┌──────────────────┐

&#x20;                        │     Frontend     │

&#x20;                        │    HTML/CSS/JS   │

&#x20;                        └────────┬─────────┘

&#x20;                                 │

&#x20;                                 │ HTTP Request

&#x20;                                 ▼

&#x20;                        ┌──────────────────┐

&#x20;                        │      Nginx       │

&#x20;                        │   Reverse Proxy  │

&#x20;                        └────────┬─────────┘

&#x20;                                 │

&#x20;                                 │ Forward Request

&#x20;                                 ▼

&#x20;                   ┌──────────────────────────┐

&#x20;                   │     FastAPI Backend      │

&#x20;                   │         Python           │

&#x20;                   │      REST APIs           │

&#x20;                   └──────────┬───────┬───────┘

&#x20;                              │       │

&#x20;                ┌─────────────┘       └─────────────┐

&#x20;                │                                   │

&#x20;                ▼                                   ▼

&#x20;       ┌──────────────────┐              ┌────────────────────┐

&#x20;       │    PostgreSQL    │              │ Security Scanner   │

&#x20;       │     Database     │              │ \& Compliance       │

&#x20;       │                  │              │ Assessment         │

&#x20;       └──────────────────┘              └────────────────────┘

&#x20;                ▲                                   │

&#x20;                │                                   │

&#x20;                └────────── Results ────────────────┘



&#x20;                            

&#x20;                        Monitoring

&#x20;                            │

&#x20;                            │ Metrics

&#x20;                            ▼

&#x20;                   ┌──────────────────┐

&#x20;                   │    Prometheus    │

&#x20;                   │     Metrics      │

&#x20;                   └────────┬─────────┘

&#x20;                            │

&#x20;                            │ Visualization

&#x20;                            ▼

&#x20;                   ┌──────────────────┐

&#x20;                   │     Grafana      │

&#x20;                   │    Dashboard     │

&#x20;                   └──────────────────┘





&#x20;                          CI/CD

&#x20;                            │

&#x20;                            ▼

&#x20;                   ┌──────────────────┐

&#x20;                   │ GitHub Actions   │

&#x20;                   │                  │

&#x20;                   │ • Build          │

&#x20;                   │ • Bandit Scan    │

&#x20;                   │ • Syntax Check   │

&#x20;                   │ • Docker Build   │

&#x20;                   │ • Health Check   │

&#x20;                   └────────┬─────────┘

&#x20;                            │

&#x20;                            │ Deploy / Build

&#x20;                            ▼

&#x20;                   ┌──────────────────┐

&#x20;                   │  Docker Services │

&#x20;                   │                  │

&#x20;                   │ Backend          │

&#x20;                   │ PostgreSQL       │

&#x20;                   │ Nginx            │

&#x20;                   │ Prometheus       │

&#x20;                   │ Grafana          │

&#x20;                   └──────────────────┘



\## 🛠️ Technology Stack



\### Backend

\- Python

\- FastAPI

\- SQLAlchemy

\- PostgreSQL

\- JWT Authentication



\### Frontend

\- HTML

\- CSS

\- JavaScript



\### Security

\- Bandit

\- Security Scanner

\- Compliance Scanner

\- JWT Authentication



\### DevOps

\- Docker

\- Docker Compose

\- Nginx

\- GitHub Actions



\### Monitoring

\- Prometheus

\- Grafana



\### Reporting

\- ReportLab

\- PDF Reports



📂 Project Structure



DevSecOps Security \& Compliance Platform/

>>>>>>> 4feb1fe (Improve architecture diagram)
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── database/
│   │   ├── models/
│   │   ├── schemas/
│   │   └── services/
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
│
├── .github/
│   └── workflows/
│       └── ci-cd.yml
│
├── Dockerfile
├── compose.yaml
├── prometheus.yml
└── README.md

## 🔐 Security Features

<<<<<<< HEAD
### JWT Authentication
=======

\## 🔐 Security Features



\### JWT Authentication

>>>>>>> 4feb1fe (Improve architecture diagram)
Users can register and login using JWT-based authentication.

Protected APIs require authentication.

<<<<<<< HEAD
### Security Scanner
The platform performs security assessment and reports detected vulnerabilities.

### Compliance Scanner
The platform evaluates configured compliance checks and identifies items that require review.

### Automated Bandit Scan
=======


\### Security Scanner

The platform performs security assessment and reports detected vulnerabilities.



\### Compliance Scanner

The platform evaluates configured compliance checks and identifies items that require review.



\### Automated Bandit Scan

>>>>>>> 4feb1fe (Improve architecture diagram)
GitHub Actions runs Bandit automatically during the CI/CD pipeline.

## 📊 Monitoring

Prometheus collects backend application metrics such as:

- HTTP request count
- Request duration
- CPU usage
- Memory usage
- Python process metrics

Grafana visualizes these metrics through the **DevSecOps Monitoring Dashboard**.

### Grafana Dashboard Panels

- HTTP Requests
- Memory Usage
- CPU Usage
- Request Rate
- Service Uptime
- Error Rate

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

## 🐳 Docker Services

The application uses Docker containers for:

- FastAPI Backend
- PostgreSQL
- Prometheus
- Grafana
- Nginx

All services communicate through the Docker network:

devsecops-network

## 🌐 API Endpoints

<<<<<<< HEAD
### Users
=======

\## 🌐 API Endpoints



\### Users

>>>>>>> 4feb1fe (Improve architecture diagram)
POST /users/register
POST /users/login
GET /users/me

<<<<<<< HEAD
### Dashboard
GET /dashboard/

### Security Scanner
=======


\### Dashboard

GET /dashboard/



\### Security Scanner

>>>>>>> 4feb1fe (Improve architecture diagram)
GET /scanner/
POST /scanner/scan
GET /scanner/history

<<<<<<< HEAD
### Compliance
=======


\### Compliance

>>>>>>> 4feb1fe (Improve architecture diagram)
POST /compliance/scan
GET /compliance/
GET /compliance/latest
GET /compliance/history

<<<<<<< HEAD
### Reports
=======


\### Reports

>>>>>>> 4feb1fe (Improve architecture diagram)
GET /reports/security
GET /reports/compliance
GET /reports/summary
GET /reports/pdf

<<<<<<< HEAD
### Monitoring
=======


\### Monitoring

>>>>>>> 4feb1fe (Improve architecture diagram)
GET /metrics
GET /health

## ▶️ Running the Project

<<<<<<< HEAD
### Create Docker Network
docker network create devsecops-network

### Start the Application
docker compose up -d

### Check Running Containers
=======

\## ▶️ Running the Project



\### Create Docker Network

docker network create devsecops-network



\### Start the Application

docker compose up -d



\### Check Running Containers

>>>>>>> 4feb1fe (Improve architecture diagram)
docker ps

## 🔗 Application URLs

<<<<<<< HEAD
### Backend
http://localhost:8000

### Nginx
http://localhost:8080

### Swagger API Documentation
http://localhost:8080/docs

### Prometheus
http://localhost:9090

### Grafana
=======

\## 🔗 Application URLs



\### Backend

http://localhost:8000



\### Nginx

http://localhost:8080



\### Swagger API Documentation

http://localhost:8080/docs



\### Prometheus

http://localhost:9090



\### Grafana

>>>>>>> 4feb1fe (Improve architecture diagram)
http://localhost:3000

## 📈 Current Test Results

The platform has been tested successfully with:

| Component | Status |
|---|---|
| Backend Health Check | ✅ PASS |
| Swagger API | ✅ PASS |
| Nginx Reverse Proxy | ✅ PASS |
| Prometheus Metrics | ✅ PASS |
| Prometheus Target | 🟢 UP |
| Grafana Dashboard | ✅ PASS |
| Service Uptime | 🟢 1 |
| Error Rate | 🟢 0 |
| GitHub Actions CI/CD | ✅ SUCCESS |
| Bandit Security Scan | ✅ SUCCESS |

## 🎯 Project Objective

The main objective of this project is to demonstrate how security, compliance, monitoring, authentication, containerization, and CI/CD can be integrated into a single DevSecOps platform.

## 👨‍💻 Author

Dharshan K
Computer Science Engineering

              
