
from fastapi import FastAPI

from src.backend.repositories.technician_repository import get_db_connection
from src.backend.routes.technician_routes import router as technician_router


app = FastAPI(title="SmartCRM - L04")

# Dang ky Routes ky thuat vien
app.include_router(technician_router)


# API trang chu
@app.get("/")
def hello():
    return {"message": "Hello Smart CRM"}


# API kiem tra ket noi SQLite
@app.get("/db-test")
def db_test():
    conn = get_db_connection()
    try:
        conn.execute("SELECT 1")
        return {"message": "SQLite connection OK"}
    finally:
        conn.close()
