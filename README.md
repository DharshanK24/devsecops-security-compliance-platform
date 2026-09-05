\# DevSecOps Security \& Compliance Platform



A containerized DevSecOps platform for automated security scanning, compliance assessment, monitoring, authentication, and report generation.



\## 🚀 Project Overview



The DevSecOps Security \& Compliance Platform integrates security and compliance checks into a software development workflow.



The platform provides:



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



```text

&#x20;                   ┌──────────────────┐

&#x20;                   │     Frontend     │

&#x20;                   │ HTML/CSS/JS      │

&#x20;                   └────────┬─────────┘

&#x20;                            │

&#x20;                            ▼

&#x20;                   ┌──────────────────┐

&#x20;                   │      Nginx       │

&#x20;                   │ Reverse Proxy    │

&#x20;                   └────────┬─────────┘

&#x20;                            │

&#x20;                            ▼

&#x20;                   ┌──────────────────┐

&#x20;                   │  FastAPI Backend  │

&#x20;                   │     Python       │

&#x20;                   └──────┬─────┬─────┘

&#x20;                          │     │

&#x20;               ┌──────────┘     └──────────┐

&#x20;               ▼                           ▼

&#x20;      ┌────────────────┐          ┌────────────────┐

&#x20;      │   PostgreSQL   │          │ Security Scan  │

&#x20;      │    Database    │          │  \& Compliance  │

&#x20;      └────────────────┘          └────────────────┘



&#x20;                   Monitoring

&#x20;                        │

&#x20;             ┌──────────┴──────────┐

&#x20;             ▼                     ▼

&#x20;      ┌──────────────┐      ┌──────────────┐

&#x20;      │ Prometheus   │ ───► │   Grafana    │

&#x20;      │   Metrics    │      │  Dashboard   │

&#x20;      └──────────────┘      └──────────────┘



&#x20;                   CI/CD

&#x20;                     │

&#x20;                     ▼

&#x20;             ┌────────────────┐

&#x20;             │ GitHub Actions │

&#x20;             │ + Bandit Scan  │

&#x20;             └────────────────┘

🛠️ Technology Stack

Backend

Python

FastAPI

SQLAlchemy

PostgreSQL

JWT Authentication

Frontend

HTML

CSS

JavaScript

Security

Bandit

Security Scanner

Compliance Scanner

JWT Authentication

DevOps

Docker

Docker Compose

Nginx

GitHub Actions

Monitoring

Prometheus

Grafana

Reporting

ReportLab

PDF Reports

📂 Project Structure

DevSecOps Security \& Compliance Platform/

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

├── .github/

│   └── workflows/

│       └── ci-cd.yml

│

├── Dockerfile

├── compose.yaml

├── prometheus.yml

└── README.md

🔐 Security Features

JWT Authentication



Users can register and login using JWT-based authentication.



Protected APIs require authentication.



Security Scanner



The platform performs security assessment and reports detected vulnerabilities.



Compliance Scanner



The platform evaluates configured compliance checks and identifies items that require review.



Automated Bandit Scan



GitHub Actions runs Bandit automatically during the CI/CD pipeline.



📊 Monitoring



Prometheus collects backend application metrics such as:



HTTP request count

Request duration

CPU usage

Memory usage

Python process metrics



Grafana visualizes these metrics through the:



DevSecOps Monitoring Dashboard



Dashboard panels include:



HTTP Requests

Memory Usage

CPU Usage

Request Rate

Service Uptime

Error Rate

🔄 CI/CD Pipeline



GitHub Actions automatically performs:



Checkout source code

Setup Python

Install dependencies

Run Bandit security scan

Python syntax check

Build Docker image

Start PostgreSQL

Start backend

Backend health check

Display backend logs if the build fails

🐳 Docker Services



The application uses Docker containers for:



FastAPI Backend

PostgreSQL

Prometheus

Grafana

Nginx



All services communicate through the Docker network:



devsecops-network

🌐 API Endpoints

Users

POST /users/register

POST /users/login

GET  /users/me

Dashboard

GET /dashboard/

Security Scanner

GET  /scanner/

POST /scanner/scan

GET  /scanner/history

Compliance

POST /compliance/scan

GET  /compliance/

GET  /compliance/latest

GET  /compliance/history

Reports

GET /reports/security

GET /reports/compliance

GET /reports/summary

GET /reports/pdf

Monitoring

GET /metrics

GET /health

▶️ Running the Project



Create the Docker network:



docker network create devsecops-network



Start the complete application:



docker compose up -d



Check running containers:



docker ps

🔗 Application URLs



Backend:



http://localhost:8000



Nginx:



http://localhost:8080



Swagger API Documentation:



http://localhost:8080/docs



Prometheus:



http://localhost:9090



Grafana:



http://localhost:3000

📈 Current Test Results



The platform has been tested successfully with:



Backend health check: PASS

Swagger API: PASS

Nginx reverse proxy: PASS

Prometheus metrics: PASS

Prometheus target: UP

Grafana dashboard: PASS

Service uptime: 1

Error rate: 0

GitHub Actions CI/CD: SUCCESS

Bandit security scan: SUCCESS

🎯 Project Objective



The main objective of this project is to demonstrate how security, compliance, monitoring, authentication, containerization, and CI/CD can be integrated into a single DevSecOps platform.



👨‍💻 Author



Dharshan K



Computer Science Engineering



