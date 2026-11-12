# SMARTCRM L04 – DOCKER DEPLOYMENT TEST REPORT

**Project:** SmartCRM – Technician Assignment and Appointment Management
**Student:** Nguyễn Ngọc Hiếu
**Student ID:** 2374802010142
**Test Date:** November 10–12, 2026
**Environment:** macOS, Docker Compose, Python 3.12, FastAPI, SQLite
**Report Version:** 1.1

---

## 1. Introduction

This report documents the Docker deployment verification, functional testing, database initialization, and security regression testing of SmartCRM L04.

The main objectives are to verify that:

- The application can be built and started using Docker Compose.
- The frontend can communicate with the backend after authentication.
- The SQLite database can be accessed and initialized successfully.
- Database migration and seed operations can be executed repeatedly without creating duplicate sample records.
- Automated tests execute successfully.
- Technician assignment and appointment management workflows operate correctly.
- Overlapping appointment requests are rejected.
- Previously identified authorization vulnerabilities remain fixed.

## 2. Test Environment

| Component | Configuration |
|---|---|
| Operating system | macOS |
| Backend | Python 3.12, FastAPI |
| Frontend | HTML, CSS, JavaScript |
| Database | SQLite |
| Deployment | Docker and Docker Compose |
| Main application URL | http://127.0.0.1:8000/app |
| Fresh Clone application URL | http://127.0.0.1:8002/app |
| API documentation | http://127.0.0.1:8000/docs |
| Fresh Clone API Health | http://127.0.0.1:8002/health |
| Test framework | pytest |
| Source control | Git and GitHub |

The application uses a Docker named volume for persistent SQLite storage.

A separate GitHub clone was created to verify that the project could be built and executed independently of the original development directory.

The final Fresh Clone verification used port 8002 to avoid conflicts with the existing Docker containers.

## 3. Docker Deployment Verification

### TC-D01: Build Docker Image

**Objective:** Verify that the SmartCRM Docker image can be built.

**Command:**

```bash
docker compose up -d --build
```

**Expected result:** Docker successfully builds the image and starts the application container.

**Actual result:** The Docker image was built and the application container started successfully.

**Status:** PASS

### TC-D02: Access SmartCRM Web Interface

**Objective:** Verify that the application is accessible from a browser.

**URL:** http://127.0.0.1:8000/app

**Expected result:** The SmartCRM web interface loads successfully.

**Actual result:** The web interface loaded successfully in the browser.

**Status:** PASS

### TC-D03: Manager Authentication

**Objective:** Verify that a configured manager can log in.

**Expected result:** Valid manager credentials are accepted and the application displays authenticated content.

**Actual result:** Manager login succeeded after rebuilding the Docker image with the updated frontend authentication logic.

**Status:** PASS

### TC-D04: Dashboard Data Retrieval

**Objective:** Verify that the frontend can retrieve protected data from the backend.

**Expected result:** The dashboard displays data after successful authentication.

**Actual result:** The dashboard displayed:

- 3 unassigned warranty tickets.
- 3 active technicians.
- 0 assignments in the dashboard statistics.

The frontend was updated to include the Bearer authentication token in protected GET requests.

**Status:** PASS

### TC-D06: Fresh Clone Docker Deployment

**Objective:** Verify that the project can be cloned from GitHub and deployed independently.

**Test environment:**

- Repository: smartcrm-2374802010142-technician-assignment.
- Branch: main.
- Working directory: smartcrm-bt3-final-check.
- Application port: 8002.
- Database: /data/smartcrm.db.

**Commands:**

```bash
git clone --branch main https://github.com/Hieu2374802010142/smartcrm-2374802010142-technician-assignment.git ~/workspace/smartcrm-bt3-final-check

cp .env.example .env

docker compose -f compose.yaml -f compose.final.yaml up -d --build
```

**Expected result:** The application can be built and started from a clean GitHub clone.

**Actual result:** The image was built successfully. The container started and reached healthy status on port 8002.

**Status:** PASS

### TC-D07: Fresh Clone Health and Web Interface

**Objective:** Verify the application health endpoint and frontend accessibility in the independent clone.

**Health check command:**

```bash
curl -i http://127.0.0.1:8002/health
```

**Actual result:**

```json
{"status":"ok","db":"up"}
```

The health endpoint returned HTTP 200.

The web interface was also checked:

```bash
curl -i http://127.0.0.1:8002/app
```

**Actual result:** HTTP 200 OK. The application returned the HTML content of the SmartCRM interface.

**Additional verification:** Docker logs confirmed successful database migration, initial seed execution, and FastAPI startup.

**Status:** PASS

### TC-D08: Database Migration and Seed Reproducibility

**Objective:** Verify that the database is initialized correctly and repeated seed execution does not create duplicate sample records.

**Initial seed result:**

```text
Khach hang moi: 3
Ky thuat vien moi: 3
Phieu bao hanh moi: 3
Seed thanh cong!
```

The initial execution created:

- 3 customers.
- 3 technicians.
- 3 warranty tickets.

**Repeated seed command:**

```bash
docker compose -f compose.yaml -f compose.final.yaml exec smartcrm python -m src.backend.seed
```

**Actual result of the second execution:**

```text
Database da co du 5 bang, khong tao lai.
Migration thanh cong.

=== KET QUA SEED ===
Khach hang moi: 0
Ky thuat vien moi: 0
Phieu bao hanh moi: 0
Seed thanh cong!
```

**Expected result:** No duplicate sample records are inserted when the seed operation is executed again.

**Actual result:** All three inserted-record counts were zero.

**Status:** PASS

## 4. Automated Testing

### TC-D05: Run pytest Test Suite

**Objective:** Verify that existing automated tests pass after the Docker deployment changes.

**Command:**

```bash
python3 -m pytest -q
```

**Expected result:** All automated tests pass.

**Actual result in the final Fresh Clone Python environment:**

```text
................................ [100%]

32 passed in 0.43s
```

**Status:** PASS

**Note:** This result was obtained using the local Python test environment in the final Fresh Clone directory. It does not establish that pytest was executed inside the Docker container.

## 5. Security Regression and Functional Testing

### 5.1. Security Regression Testing

The following tests were performed against the running application at `127.0.0.1:8000`, without an authentication token.

### TC-S01: Unauthorized Access to Unassigned Tickets

**Related defect:** BUG-02

**Endpoint:** `GET /api/tickets/unassigned`

**Command:**

```bash
curl -i http://127.0.0.1:8000/api/tickets/unassigned
```

**Expected result:** HTTP 401 Unauthorized.

**Actual result:**

```text
HTTP/1.1 401 Unauthorized
{"detail":"Chua dang nhap"}
```

**Status:** PASS

### TC-S02: Unauthorized Access to Assignments

**Related defect:** BUG-01

**Endpoint:** `GET /api/tickets/assignments`

**Command:**

```bash
curl -i http://127.0.0.1:8000/api/tickets/assignments
```

**Expected result:** HTTP 401 Unauthorized.

**Actual result:**

```text
HTTP/1.1 401 Unauthorized
{"detail":"Chua dang nhap"}
```

**Status:** PASS

### TC-S03: Unauthorized Access to Technicians

**Related defect:** BUG-03

**Endpoint:** `GET /api/technicians`

**Command:**

```bash
curl -i http://127.0.0.1:8000/api/technicians
```

**Expected result:** HTTP 401 Unauthorized.

**Actual result:**

```text
HTTP/1.1 401 Unauthorized
{"detail":"Chua dang nhap"}
```

**Status:** PASS

### 5.2. Fresh Clone Functional Testing

The following functional checks were performed through the SmartCRM interface running on port 8002.

### TC-F01: Manager Login and Dashboard Access

**Objective:** Verify that the manager can access the application after authentication.

**Expected result:** The manager can log in and view the dashboard.

**Actual result:** Manager login succeeded. The dashboard displayed the warranty-ticket and technician statistics.

**Status:** PASS

### TC-F02: Technician Assignment

**Objective:** Verify that a warranty ticket can be assigned to an active technician.

**Expected result:** The system accepts a valid technician assignment.

**Actual result:** A technician assignment was successfully created for the OPPO Reno 8 warranty ticket and technician Nguyen Van An.

**Status:** PASS

### TC-F03: Appointment Creation

**Objective:** Verify that a manager can create an appointment for an existing assignment.

**Test data:**

- Assignment: Assignment 1 – OPPO Reno 8.
- Technician: Nguyen Van An.
- Appointment type: Receive device.
- Date: November 12, 2026.
- Start time: 21:21.
- End time: 23:21.

**Expected result:** The system saves the appointment successfully.

**Actual result:** The application displayed a successful appointment creation message and returned appointment ID 1.

**Status:** PASS

### TC-F04: Overlapping Appointment Rejection

**Objective:** Verify that the system rejects an appointment that overlaps an existing appointment for the same technician.

**Existing appointment:**

- Date: November 12, 2026.
- Time: 21:21–23:21.

**Overlapping appointment request:**

- Date: November 12, 2026.
- Time: 22:00–23:00.

**Expected result:** The application rejects the overlapping appointment and displays an appropriate conflict message.

**Actual result:**

```text
Loi: Lich hen bi trung voi lich cua ky thuat vien.
```

The application rejected the request.

**Status:** PASS

### TC-F05: Database Verification After Rejected Appointment

**Objective:** Verify that a rejected overlapping appointment is not inserted into the database.

**Command:**

```bash
docker compose -f compose.yaml -f compose.final.yaml exec smartcrm python -c "import sqlite3; c=sqlite3.connect('/data/smartcrm.db'); print('Tong so lich hen:', c.execute('SELECT COUNT(*) FROM lich_hen').fetchone()[0]); c.close()"
```

**Expected result:** The database contains only the original appointment.

**Actual result:**

```text
Tong so lich hen: 1
```

The database still contained only one appointment after the overlapping request was rejected.

**Status:** PASS

## 6. Test Result Summary

| Test ID | Description | Result |
|---|---|---|
| TC-D01 | Docker image build and startup | PASS |
| TC-D02 | Web interface accessibility | PASS |
| TC-D03 | Manager authentication | PASS |
| TC-D04 | Authenticated dashboard data retrieval | PASS |
| TC-D05 | Final Fresh Clone pytest suite | PASS |
| TC-D06 | Independent Fresh Clone deployment | PASS |
| TC-D07 | Fresh Clone health and web interface | PASS |
| TC-D08 | Migration and repeated seed verification | PASS |
| TC-S01 | Unauthorized unassigned-ticket access | PASS |
| TC-S02 | Unauthorized assignment-list access | PASS |
| TC-S03 | Unauthorized technician-list access | PASS |
| TC-F01 | Fresh Clone manager login | PASS |
| TC-F02 | Technician assignment | PASS |
| TC-F03 | Appointment creation | PASS |
| TC-F04 | Overlapping appointment rejection | PASS |
| TC-F05 | Database verification after rejected appointment | PASS |

**Summary:**

- Docker deployment and functional verification: 7/7 PASS.
- Fresh Clone database initialization and repeatability: 1/1 PASS.
- Local automated test suite: 32/32 PASS.
- Security regression checks: 3/3 PASS.
- Fresh Clone functional checks: 5/5 PASS.
- Total documented verification cases: 16/16 PASS.

The 32 pytest tests are reported separately and are not counted as 32 additional verification cases.

## 7. Defects and Fixes

### Frontend Authentication Issue

**Problem:** After login, some protected GET requests did not include the required authentication header, causing HTTP 401 responses.

**Root cause:** The frontend did not consistently attach the Bearer token to protected API requests.

**Resolution:** Updated the frontend request logic to use `getAuthHeaders()` for the affected GET requests.

**Verification:** The application was rebuilt using Docker Compose. Manager login and authenticated dashboard data retrieval succeeded.

**Status:** FIXED

### Previous BT3 Authorization Defects

The three previously identified authorization defects were rechecked against the Docker deployment.

All three protected endpoints returned HTTP 401 when accessed without authentication.

**Status:** REGRESSION TESTS PASSED

## 8. Limitations and Pending Tests

Although the documented deployment and functional checks passed, some additional tests have not yet been completed.

The following checks remain pending:

- Verify database persistence after container recreation.
- Test invalid or expired authentication tokens.
- Verify comprehensive role-specific access restrictions.
- Test simultaneous appointment requests under concurrent load.
- Run a Docker image vulnerability scan.

**Dependency Security Audit:**

A dependency audit was completed on November 12, 2026 using:

```bash
python3 -m pip_audit -r requirements.txt
```

**Actual result:**

```text
No known vulnerabilities found
```

**Status:** PASS

**Evidence:** `docs/screenshots/Security_Dependency_Audit.png`

This dependency audit does not constitute a Docker image vulnerability scan.

The pending checks should be completed before production deployment.

## 9. Conclusion

The SmartCRM L04 Docker deployment passed the documented build, accessibility, authentication, dashboard, and unauthorized-access checks.

The final independent Fresh Clone verification confirmed that the project could be cloned from GitHub, built with Docker Compose, initialized with SQLite, and started successfully.

Database migration and repeated seed execution were successful. The second seed operation inserted no additional sample records.

The final Fresh Clone automated test suite completed with 32 passing tests.

Functional testing also confirmed successful manager authentication, technician assignment, appointment creation, and rejection of overlapping appointments. Database verification confirmed that rejected overlapping appointments were not inserted.

All three previously identified BT3 authorization defects passed their unauthenticated-access regression tests.

The dependency audit reported no known vulnerabilities at the time of testing.

These results support the use of the SmartCRM L04 deployment for course-project demonstration. Additional security, concurrency, and operational testing is recommended before production use.