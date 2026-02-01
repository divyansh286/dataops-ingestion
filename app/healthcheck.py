import os
import sys
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("healthcheck")

def main():
    # CI MODE → skip DB entirely
    if os.getenv("CI") == "true":
        logger.info("CI mode detected – skipping database connectivity check")
        sys.exit(0)

    # NON-CI MODE → real DB check
    try:
        from app.db import get_connection
        conn = get_connection()
        conn.close()
        logger.info("Healthcheck passed – database connection successful")
        sys.exit(0)
    except Exception as e:
        logger.error(f"Healthcheck failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

