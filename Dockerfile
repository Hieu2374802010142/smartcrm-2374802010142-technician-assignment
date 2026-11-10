FROM python:3.12-slim

WORKDIR /app

# Cai dat cac thu vien Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Sao chep ma nguon va schema
COPY src/ ./src/
COPY docs/database/schema-l04.sql ./docs/database/schema-l04.sql

# Cau hinh ung dung
ENV PYTHONUNBUFFERED=1
ENV SMARTCRM_DB_PATH=/data/smartcrm.db

EXPOSE 8000

# Khoi tao database va chay FastAPI
CMD ["sh", "-c", "python -m src.backend.seed && exec uvicorn src.backend.main:app --host 0.0.0.0 --port 8000"]
