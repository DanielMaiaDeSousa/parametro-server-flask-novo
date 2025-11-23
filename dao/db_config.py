import sqlite3
import psycopg
# path / url de conexão
DB_PATH ="postgresql://neondb_owner:npg_iBuW8wRrOqf2@ep-calm-mountain-ahjif78i-pooler.c-3.us-east-1.aws.neon.tech/neondb?sslmode=require"
def get_connection():
    return psycopg.connect(DB_PATH)

