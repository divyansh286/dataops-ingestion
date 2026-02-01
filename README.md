# DataOps Ingestion Pipeline (Docker + Azure)

## Overview
This project implements a **production-ready DataOps ingestion pipeline** using Python, Docker, and Azure services.
It ingests CSV data into **Azure SQL Database**, handles idempotency, and is deployable via **Azure Container Registry (ACR)** and **Azure Container Instances (ACI)**.

Designed with real-world **Data Engineer / DataOps** practices:
- Containerized ingestion
- Environment-based configuration
- Health checks
- Cloud deployment

---

## Architecture
```
CSV → Python Ingestion → Azure SQL Database
        |
        └── Docker Container
              └── Azure Container Registry
                    └── Azure Container Instance
```

---

## Tech Stack
- Python 3.10
- pyodbc
- Docker
- Azure SQL Database
- Azure Container Registry (ACR)
- Azure Container Instances (ACI)

---

## Project Structure
```
dataops-python/
│
├── app/
│   ├── ingest.py          # Data ingestion logic
│   ├── db.py              # Azure SQL connection
│   ├── logger.py          # Centralized logging
│   └── healthcheck.py     # Runtime health check
│
├── data/
│   └── sales.csv          # Sample input data
│
├── Dockerfile
├── requirements.txt
├── .dockerignore
└── README.md
```

---

## Environment Variables
The pipeline uses environment variables (never hardcoded):

```
DB_SERVER=your_server.database.windows.net
DB_NAME=your_database
DB_USER=sql_user@server
DB_PASSWORD=********
```

---

## Local Execution
```bash
python -m app.ingest
```

---

## Docker Build & Run
```bash
docker build -t dataops-ingestion .
docker run --env-file .env dataops-ingestion
```

---

## Azure Deployment Flow
1. Build Docker image
2. Push image to Azure Container Registry
3. Run container in Azure Container Instance
4. Ingestion executes once and exits

---

## Key Features
- Idempotent ingestion (duplicate-safe)
- Secure secrets via environment variables
- SQL Server ODBC Driver 18
- Cloud-ready container image
- Health check support

---

## Status
- Local execution verified
- Docker image built successfully
- Image pushed to ACR
- ACI deployment tested

---

## Author
Divyansh  
(Data Engineering / DataOps Project)
