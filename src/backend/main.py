
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse

from src.backend.repositories.technician_repository import get_db_connection
from src.backend.routes.technician_routes import router as technician_router
from src.backend.routes.ticket_routes import router as ticket_router
from src.backend.routes.auth_routes import router as auth_router


# Khoi tao ung dung FastAPI
app = FastAPI(title="SmartCRM - L04")


# Dang ky Routes ky thuat vien
app.include_router(technician_router)

# Dang ky Routes phieu bao hanh
app.include_router(ticket_router)

# Dang ky API dang nhap
app.include_router(auth_router)


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


# API kiem tra suc khoe ung dung va SQLite
@app.get("/health")
def health_check():
    conn = None

    try:
        conn = get_db_connection()
        conn.execute("SELECT 1")

        return {
            "status": "ok",
            "db": "up"
        }

    except Exception:
        return JSONResponse(
            status_code=503,
            content={
                "status": "error",
                "db": "down"
            }
        )

    finally:
        if conn is not None:
            conn.close()


# Duong dan giao dien SmartCRM L04
FRONTEND_DIR = Path(__file__).resolve().parents[1] / "frontend"


# API hien thi giao dien SmartCRM
@app.get("/app", include_in_schema=False)
def show_frontend():
    return FileResponse(FRONTEND_DIR / "index.html")
