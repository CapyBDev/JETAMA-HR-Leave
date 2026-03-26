import sqlite3
import pandas as pd
from sqlalchemy import create_engine

# ---------- CONFIG ----------
SQLITE_DB = "database.db"
POSTGRES_URL = "postgresql://claim_db_iw7g_user:VqDnpd2yPdNqtEKGla3esCEUMlEa3Kq7@dpg-d71nmima2pns73fas9b0-a.singapore-postgres.render.com/claim_db_iw7g"
# ----------------------------

# Connect SQLite
sqlite_conn = sqlite3.connect(SQLITE_DB)

# Connect PostgreSQL
pg_engine = create_engine(POSTGRES_URL)

# Tables to migrate (ORDER MATTERS)
tables = [
    "users",
    "departments",
    "holidays",
    "leave_applications",
    "leaves",
    "leave_logs",
    "mc_records",
    "settings"
]

for table in tables:
    print(f"Migrating {table}...")
    df = pd.read_sql_query(f"SELECT * FROM {table}", sqlite_conn)

    df.to_sql(
        table,
        pg_engine,
        if_exists="append",   
        index=False
    )

print(" Migration completed successfully")
