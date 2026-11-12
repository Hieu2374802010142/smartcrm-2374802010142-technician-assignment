# SMARTCRM L04 – API DOCUMENTATION

**Project:** SmartCRM – Technician Assignment and Appointment Management
**Student:** Nguyễn Ngọc Hiếu
**Student ID:** 2374802010142
**Date:** November 12, 2026
**Version:** 1.0 – BT3 API Documentation
**Framework:** FastAPI
**Database:** SQLite
**API Format:** REST / JSON

## 1. Introduction

This document describes the REST API operations implemented in SmartCRM L04.

The application supports administrator authentication, technician management, warranty ticket management, technician assignments, appointment scheduling, and system health checks.

The documentation covers 17 API operations exposed through the application's OpenAPI schema.

Each operation includes its HTTP method, endpoint, purpose, authentication requirements, request data, successful response, and possible error responses.

## 2. Base URL and Authentication

### 2.1 Base URL

Standard local deployment:

`http://127.0.0.1:8000`

Fresh Clone Docker deployment:

`http://127.0.0.1:8001`

These URLs refer to local development and verification environments.

### 2.2 Authentication

Protected management endpoints require a bearer token obtained from the login API.

**Authorization header:**

`Authorization: Bearer <access_token>`

The current application supports the `manager` role.

Authentication tokens are stored in application memory and expire after 60 minutes.

### 2.3 Common HTTP Status Codes

| Status Code | Meaning |
|---|---|
| 200 | Request completed successfully |
| 201 | Resource created successfully |
| 400 | Invalid business data |
| 401 | Missing, invalid, or expired authentication |
| 403 | Insufficient permission |
| 404 | Requested resource not found |
| 409 | Business rule or database conflict |
| 422 | Request validation failed |
| 500 | Internal server error |
| 503 | Service or configuration unavailable |

The exact status codes depend on the operation and error condition.

---

## 3. Authentication API

### API-01: Administrator Login

**1. HTTP Method:** POST

**2. Endpoint:** `/api/auth/login`

**3. Purpose:** Authenticate the administrator and issue a bearer token.

**4. Authentication:** Not required.

**5. Request Body:**

```json
{
  "username": "manager",
  "password": "<administrator-password>"
}
```

Both fields are required strings. The username is illustrative and must match the configured administrator account.

**6. Successful Response – HTTP 200:**

```json
{
  "access_token": "<generated-token>",
  "token_type": "bearer",
  "role": "manager"
}
```

**7. Error Responses:**

- 401: Incorrect username or password.
- 422: Missing or invalid request fields.
- 503: Administrator account configuration is missing or invalid.

---

## 4. Technician Management APIs

### API-02: Get All Technicians

**1. HTTP Method:** GET

**2. Endpoint:** `/api/technicians`

**3. Purpose:** Retrieve the list of technicians.

**4. Authentication:** Required – manager bearer token.

**5. Request:** No request body or query parameters.

**6. Successful Response – HTTP 200:**

```json
{
  "technicians": [
    {
      "ma_ky_thuat_vien": 1,
      "ho_ten": "Technician A",
      "so_dien_thoai": "0900000000",
      "chuyen_mon": "Mobile repair",
      "dang_hoat_dong": 1
    }
  ]
}
```

The record shown is illustrative.

**7. Error Responses:**

- 401: Missing or invalid token.
- 403: User does not have manager permission.
- 500: Database operation failed.

### API-03: Create Technician

**1. HTTP Method:** POST

**2. Endpoint:** `/api/technicians`

**3. Purpose:** Add a new technician.

**4. Authentication:** Required – manager bearer token.

**5. Request Body:**

```json
{
  "ho_ten": "Technician B",
  "so_dien_thoai": "0911111111",
  "chuyen_mon": "Hardware repair",
  "dang_hoat_dong": true
}
```

`ho_ten` is required. Other fields are optional; `dang_hoat_dong` defaults to `true`.

**6. Successful Response – HTTP 201:**

```json
{
  "message": "Them ky thuat vien thanh cong",
  "ma_ky_thuat_vien": 4
}
```

**7. Error Responses:**

- 400: Invalid business data.
- 401: Missing or invalid token.
- 403: Insufficient permission.
- 409: Data integrity conflict.
- 422: Invalid request structure or field type.
- 500: Database error.

### API-04: Update Technician

**1. HTTP Method:** PUT

**2. Endpoint:** `/api/technicians/{technician_id}`

**3. Purpose:** Update an existing technician's information and activity status.

**4. Authentication:** Required – manager bearer token.

**5. Request:**

Path parameter: `technician_id` – technician identifier.

Request body:

```json
{
  "ho_ten": "Technician B Updated",
  "so_dien_thoai": "0911111111",
  "chuyen_mon": "Software repair",
  "dang_hoat_dong": true
}
```

**6. Successful Response – HTTP 200:**

```json
{
  "message": "Cap nhat ky thuat vien thanh cong",
  "ma_ky_thuat_vien": 4
}
```

**7. Error Responses:**

- 400: Invalid technician identifier or business data.
- 401: Missing or invalid token.
- 403: Insufficient permission.
- 404: Technician not found.
- 409: Data integrity conflict.
- 422: Invalid request data.
- 500: Database error.

### API-05: Deactivate Technician

**1. HTTP Method:** DELETE

**2. Endpoint:** `/api/technicians/{technician_id}`

**3. Purpose:** Deactivate a technician without permanently deleting the database record.

**4. Authentication:** Required – manager bearer token.

**5. Request:** Path parameter `technician_id`. No request body.

**6. Successful Response – HTTP 200:**

```json
{
  "message": "Da ngung hoat dong ky thuat vien",
  "ma_ky_thuat_vien": 4
}
```

The implementation performs a soft delete by setting `dang_hoat_dong = 0`.

**7. Error Responses:**

- 400: Invalid technician identifier.
- 401: Missing or invalid token.
- 403: Insufficient permission.
- 404: Technician not found.
- 409: Business or database conflict.
- 422: Invalid path parameter.
- 500: Database error.

---

## 5. Warranty Ticket APIs

### API-06: Get All Warranty Tickets

**1. HTTP Method:** GET

**2. Endpoint:** `/api/tickets`

**3. Purpose:** Retrieve warranty tickets and their related customer information.

**4. Authentication:** Required – manager bearer token.

**5. Request:** No request body.

**6. Successful Response – HTTP 200:**

```json
{
  "tickets": [
    {
      "ma_phieu": 1,
      "ma_khach_hang": 1,
      "ten_thiet_bi": "iPhone",
      "trang_thai": "Mới",
      "ngay_tao": "2026-11-10",
      "ten_khach_hang": "Customer A"
    }
  ],
  "total": 1
}
```

**7. Error Responses:**

- 401: Missing or invalid token.
- 403: Insufficient permission.
- 500: Database error.

### API-07: Create Warranty Ticket

**1. HTTP Method:** POST

**2. Endpoint:** `/api/tickets`

**3. Purpose:** Create a warranty ticket for an existing customer.

**4. Authentication:** Required – manager bearer token.

**5. Request Body:**

```json
{
  "ma_khach_hang": 1,
  "ten_thiet_bi": "Samsung Galaxy"
}
```

`ma_khach_hang` must be a positive integer. `ten_thiet_bi` must be a nonempty string.

**6. Successful Response – HTTP 201:**

```json
{
  "message": "Tao phieu bao hanh thanh cong",
  "ma_phieu": 5
}
```

**7. Error Responses:**

- 400: Invalid business data.
- 401: Missing or invalid token.
- 403: Insufficient permission.
- 404: Customer not found.
- 409: Data conflict, if applicable.
- 422: Invalid request structure.
- 500: Database error.

### API-08: Get Warranty Ticket by ID

**1. HTTP Method:** GET

**2. Endpoint:** `/api/tickets/{ticket_id}`

**3. Purpose:** Retrieve details of one warranty ticket.

**4. Authentication:** Required – manager bearer token.

**5. Request:** Path parameter `ticket_id`.

**6. Successful Response – HTTP 200:**

```json
{
  "ma_phieu": 1,
  "ma_khach_hang": 1,
  "ten_thiet_bi": "iPhone",
  "trang_thai": "Mới",
  "ngay_tao": "2026-11-10"
}
```

**7. Error Responses:**

- 401: Missing or invalid token.
- 403: Insufficient permission.
- 404: Ticket not found.
- 422: Invalid path parameter.
- 500: Database error.

### API-09: Update Warranty Ticket

**1. HTTP Method:** PUT

**2. Endpoint:** `/api/tickets/{ticket_id}`

**3. Purpose:** Update an existing warranty ticket before it has been assigned.

**4. Authentication:** Required – manager bearer token.

**5. Request:**

Path parameter: `ticket_id`.

Request body:

```json
{
  "ma_khach_hang": 1,
  "ten_thiet_bi": "iPhone 15"
}
```

**6. Successful Response – HTTP 200:**

```json
{
  "message": "Cap nhat phieu thanh cong",
  "ma_phieu": 1
}
```

**7. Error Responses:**

- 400: Invalid business data.
- 401: Missing or invalid token.
- 403: Insufficient permission.
- 404: Ticket or related customer not found.
- 409: Ticket cannot be edited because of its state or assignment history.
- 422: Invalid request data.
- 500: Database error.

### API-10: Delete Warranty Ticket

**1. HTTP Method:** DELETE

**2. Endpoint:** `/api/tickets/{ticket_id}`

**3. Purpose:** Delete an unassigned warranty ticket.

**4. Authentication:** Required – manager bearer token.

**5. Request:** Path parameter `ticket_id`. No request body.

**6. Successful Response – HTTP 200:**

```json
{
  "message": "Xoa phieu bao hanh thanh cong",
  "ma_phieu": 1
}
```

Unlike technician deactivation, this operation performs a database DELETE when the ticket is eligible.

**7. Error Responses:**

- 401: Missing or invalid token.
- 403: Insufficient permission.
- 404: Ticket not found.
- 409: Ticket cannot be deleted because of its state or assignment history.
- 422: Invalid path parameter.
- 500: Database error.

### API-11: Get Unassigned Warranty Tickets

**1. HTTP Method:** GET

**2. Endpoint:** `/api/tickets/unassigned`

**3. Purpose:** Retrieve new warranty tickets without an active technician assignment.

**4. Authentication:** Required – manager bearer token.

**5. Request:** No request body.

**6. Successful Response – HTTP 200:**

```json
{
  "tickets": [
    {
      "ma_phieu": 1,
      "ten_thiet_bi": "iPhone",
      "trang_thai": "Mới",
      "ngay_tao": "2026-11-10",
      "ten_khach_hang": "Customer A",
      "so_dien_thoai": "0900000000"
    }
  ],
  "total": 1
}
```

**7. Error Responses:**

- 401: Missing or invalid token.
- 403: Insufficient permission.
- 500: Database error.

**Security note:** This endpoint was protected during the BUG-02 fix.

---

## 6. Technician Assignment APIs

### API-12: Assign Technician to Warranty Ticket

**1. HTTP Method:** POST

**2. Endpoint:** `/api/tickets/{ticket_id}/assign`

**3. Purpose:** Assign an active technician to a new warranty ticket.

**4. Authentication:** Required – manager bearer token.

**5. Request:**

Path parameter: `ticket_id`.

Request body:

```json
{
  "ma_ky_thuat_vien": 1
}
```

The technician identifier must be a positive integer.

**6. Successful Response – HTTP 200:**

```json
{
  "message": "Phan cong ky thuat vien thanh cong",
  "ma_phan_cong": 1,
  "ma_phieu": 1,
  "ma_ky_thuat_vien": 1
}
```

The ticket state is updated to `Đã phân công`.

**7. Error Responses:**

- 400: Invalid business data.
- 401: Missing or invalid token.
- 403: Insufficient permission.
- 404: Ticket or technician not found.
- 409: Ticket is not new, technician is inactive, or assignment conflict occurs.
- 422: Invalid request data.
- 500: Database error.

### API-13: Get Active Technician Assignments

**1. HTTP Method:** GET

**2. Endpoint:** `/api/tickets/assignments`

**3. Purpose:** Retrieve active technician assignments and related ticket information.

**4. Authentication:** Required – manager bearer token.

**5. Request:** No request body.

**6. Successful Response – HTTP 200:**

```json
{
  "assignments": [
    {
      "ma_phan_cong": 1,
      "ma_phieu": 1,
      "ten_thiet_bi": "iPhone",
      "ma_ky_thuat_vien": 1,
      "ten_ky_thuat_vien": "Technician A"
    }
  ],
  "total": 1
}
```

**7. Error Responses:**

- 401: Missing or invalid token.
- 403: Insufficient permission.
- 500: Database error.

**Security note:** This endpoint was protected during the BUG-01 fix.

---

## 7. Appointment Scheduling API

### API-14: Create Appointment

**1. HTTP Method:** POST

**2. Endpoint:** `/api/tickets/appointments`

**3. Purpose:** Create an appointment for an active technician assignment while preventing overlapping schedules.

**4. Authentication:** Required – manager bearer token.

**5. Request Body:**

```json
{
  "ma_phan_cong": 1,
  "ngay_hen": "2026-11-15",
  "gio_bat_dau": "09:00",
  "gio_ket_thuc": "10:00",
  "loai_lich_hen": "Giao máy"
}
```

Required fields:

- `ma_phan_cong`: positive integer.
- `ngay_hen`: date.
- `gio_bat_dau`: start time.
- `gio_ket_thuc`: end time.
- `loai_lich_hen`: nonempty string.

The end time must be later than the start time.

**6. Successful Response – HTTP 200:**

```json
{
  "message": "Dat lich hen thanh cong",
  "ma_lich_hen": 1,
  "ma_phan_cong": 1
}
```

**7. Error Responses:**

- 400: Invalid appointment time range or appointment type.
- 401: Missing or invalid token.
- 403: Insufficient permission.
- 404: Active assignment not found.
- 409: Appointment overlaps an existing active appointment for the same technician.
- 422: Invalid request data.
- 500: Database error.

---

## 8. System APIs

### API-15: Root Endpoint

**1. HTTP Method:** GET

**2. Endpoint:** `/`

**3. Purpose:** Return a basic application greeting.

**4. Authentication:** Not required.

**5. Request:** No parameters or request body.

**6. Successful Response – HTTP 200:**

```json
{
  "message": "Hello Smart CRM"
}
```

**7. Error Responses:** No application-specific error response is defined for this endpoint. Unexpected server errors may return HTTP 500.

### API-16: SQLite Connection Test

**1. HTTP Method:** GET

**2. Endpoint:** `/db-test`

**3. Purpose:** Check whether the application can establish a SQLite connection and execute a simple SQL query.

**4. Authentication:** Not required.

**5. Request:** No parameters or request body.

**6. Successful Response – HTTP 200:**

```json
{
  "message": "SQLite connection OK"
}
```

**7. Error Responses:** Database connection or query failures may result in an unhandled server error, typically HTTP 500. No custom failure response is implemented for this endpoint.

### API-17: Application Health Check

**1. HTTP Method:** GET

**2. Endpoint:** `/health`

**3. Purpose:** Check application availability and SQLite connectivity.

**4. Authentication:** Not required.

**5. Request:** No parameters or request body.

**6. Successful Response – HTTP 200:**

```json
{
  "status": "ok",
  "db": "up"
}
```

**7. Error Response – HTTP 503:**

```json
{
  "status": "error",
  "db": "down"
}
```

The endpoint returns a general failure message without exposing database exception details.

---

## 9. Additional Frontend Route

The application also provides:

**GET `/app`**

This route serves the SmartCRM HTML frontend.

It is defined with `include_in_schema=False`, so it is not included in the 17 OpenAPI operations documented above.

The frontend is accessible at:

- Standard local deployment: `http://127.0.0.1:8000/app`
- Fresh Clone Docker deployment: `http://127.0.0.1:8001/app`

## 10. API Security Notes

All technician and warranty management endpoints require manager authentication.

The backend validates bearer tokens and rejects unauthorized requests.

Three authorization issues identified during BT3 were fixed:

- BUG-01: Assignments API access control.
- BUG-02: Unassigned tickets API access control.
- BUG-03: Technician list API access control.

The relevant regression tests confirmed HTTP 401 responses for unauthenticated access.

Input validation is implemented through Pydantic and business-service checks.

Repository SQL statements use parameterized queries to handle dynamic values.

The API is intended for the verified local course-project environment. Additional hardening is required before public production deployment.

## 11. Verification and References

**API specification:** FastAPI-generated OpenAPI schema at `/openapi.json`.

**Interactive documentation:** FastAPI Swagger UI at `/docs`.

**Source code:**

- `src/backend/main.py`
- `src/backend/routes/auth_routes.py`
- `src/backend/routes/technician_routes.py`
- `src/backend/routes/ticket_routes.py`
- `src/backend/services/technician_service.py`
- `src/backend/services/ticket_service.py`
- `src/backend/repositories/technician_repository.py`
- `src/backend/repositories/ticket_repository.py`
- `src/backend/auth/security.py`

**Testing and security evidence:**

- `docs/test-plan-bt3.md`
- `docs/test-report.md`
- `docs/test-report-docker.md`
- `docs/bug-log-bt3.md`
- `docs/checklist-bao-mat.md`

## 12. Conclusion

This document describes the 17 API operations exposed by SmartCRM L04.

The documented functions cover administrator login, technician CRUD operations, warranty ticket CRUD operations, technician assignments, appointment scheduling, and system monitoring.

The documentation is based on the reviewed FastAPI implementation and OpenAPI specification.

It serves as the API reference for BT3 testing, deployment verification, and the final course-project submission.