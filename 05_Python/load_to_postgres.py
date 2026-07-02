import pandas as pd
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="apexiq_enterprise",
    user="postgres",
    password="Akshay@12345",
    port="5432"
)

print("✅ PostgreSQL Connected Successfully")

conn.close()