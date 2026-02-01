import sys
from app.db import get_connection
from app.logger import get_logger

logger = get_logger(__name__)

def run_healthcheck():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT 1;")
        cursor.fetchone()
        conn.close()

        logger.info("Healthcheck passed: Database connection successful")
        sys.exit(0)

    except Exception as e:
        logger.error(f"Healthcheck failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    run_healthcheck()
