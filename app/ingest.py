import pandas as pd
from app.db import get_connection
from app.logger import get_logger

logger = get_logger()

def ingest_data():
    df = pd.read_csv("data/sales.csv")

    inserted = 0
    skipped = 0

    conn = get_connection()
    cursor = conn.cursor()

    for _, row in df.iterrows():
        cursor.execute(
            """
            IF NOT EXISTS (
                SELECT 1 FROM sales_data WHERE order_id = ?
            )
            INSERT INTO sales_data (
                order_id,
                product,
                quantity,
                price,
                order_date
            )
            VALUES (?, ?, ?, ?, ?)
            """,
            row["order_id"],
            row["order_id"],
            row["product"],
            int(row["quantity"]),
            float(row["price"]),
            row["order_date"]
        )

        if cursor.rowcount == 1:
            inserted += 1
        else:
            skipped += 1

    conn.commit()
    conn.close()

    logger.info(f"Ingestion completed | inserted={inserted} | skipped={skipped}")

if __name__ == "__main__":
    ingest_data()
