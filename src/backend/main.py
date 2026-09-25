from fastapi import FastAPI
import sqlite3

app = FastAPI(title="SmartCRM - L04")


def get_db_connection():
    return sqlite3.connect("smartcrm.db")


@app.get("/")
def hello():
    return {"message": "Hello Smart CRM"}


@app.get("/db-test")
def db_test():
    conn = get_db_connection()
    conn.execute("SELECT 1")
    conn.close()
    return {"message": "SQLite connection OK"}
