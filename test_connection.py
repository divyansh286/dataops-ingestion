import pyodbc

conn = pyodbc.connect(
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=dataopsadmin.database.windows.net;"
    "DATABASE=dataopsdb;"
    "UID=dataops-sql-server;"
    "PWD=TYUIop@123*5259a;"
    "Encrypt=yes;"
    "TrustServerCertificate=no;"
)

cursor = conn.cursor()
cursor.execute("SELECT COUNT(*) FROM sales_data;")
print("Row count:", cursor.fetchone()[0])

conn.close()



