FROM python:3.10-slim

# Prevent Python from buffering logs
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system dependencies for pyodbc
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    curl \
    unixodbc \
    unixodbc-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Microsoft ODBC Driver 18 (signed-by fix)
RUN apt-get update && apt-get install -y curl gnupg ca-certificates \
    && curl -sSL https://packages.microsoft.com/keys/microsoft.asc \
       | gpg --dearmor \
       | tee /usr/share/keyrings/microsoft-prod.gpg > /dev/null \
    && echo "deb [arch=amd64 signed-by=/usr/share/keyrings/microsoft-prod.gpg] https://packages.microsoft.com/debian/11/prod bullseye main" \
       > /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update \
    && ACCEPT_EULA=Y apt-get install -y msodbcsql18 \
    && rm -rf /var/lib/apt/lists/*



# Copy requirements and install Python deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app ./app
COPY data ./data

# Default command
CMD ["python", "-m", "app.ingest"]

#Health check
HEALTHCHECK --interval=30s --timeout=10s --retries=3 \
  CMD python -m app.healthcheck || exit 1

