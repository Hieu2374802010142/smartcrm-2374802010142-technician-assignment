# SMARTCRM L04 – DOCKER DEPLOYMENT TEST REPORT

**Project:** SmartCRM – Technician Assignment and Appointment Management  
**Student:** Nguyễn Ngọc Hiếu  
**Student ID:** 2374802010142  
**Test Date:** November 10, 2026  
**Environment:** macOS, Docker Compose, Python 3.12, FastAPI, SQLite  
**Report Version:** 1.0

---

## 1. Introduction

This report documents the deployment verification and security regression testing of SmartCRM L04 during the Docker deployment phase.

The main objectives are to verify that:

- The application can be built and started using Docker Compose.
- The frontend can communicate with the backend after authentication.
- The SQLite database can be accessed by the application.
- Automated tests execute successfully.
- Previously identified authorization vulnerabilities remain fixed in the Docker environment.

## 2. Test Environment

| Component | Configuration |
|---|---|
| Operating system | macOS |
| Backend | Python 3.12, FastAPI |
| Frontend | HTML, CSS, JavaScript |
| Database | SQLite |
| Deployment | Docker and Docker Compose |
| Application URL | http://127.0.0.1:8000/app |
| API documentation | http://127.0.0.1:8000/docs |
| Test framework | pytest |
| Source control | Git and GitHub |

The application uses a Docker named volume for persistent SQLite storage.

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

## 4. Automated Testing

### TC-D05: Run pytest Test Suite

**Objective:** Verify that existing automated tests pass after the Docker deployment changes.

**Command:**

```bash
python3 -m pytest -q
```

**Expected result:** All automated tests pass.

**Actual result:**

```text
................................ [100%]
32 passed in 0.27s
```

**Status:** PASS

**Note:** This result was obtained from the local Python test environment. It does not by itself establish that pytest was executed inside the Docker container.

## 5. Security Regression Testing

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

## 6. Test Result Summary

| Test ID | Description | Result |
|---|---|---|
| TC-D01 | Docker image build and startup | PASS |
| TC-D02 | Web interface accessibility | PASS |
| TC-D03 | Manager authentication | PASS |
| TC-D04 | Authenticated dashboard data retrieval | PASS |
| TC-D05 | Local pytest test suite | PASS |
| TC-S01 | Unauthorized unassigned-ticket access | PASS |
| TC-S02 | Unauthorized assignment-list access | PASS |
| TC-S03 | Unauthorized technician-list access | PASS |

**Summary:**

- Deployment and functional verification: 4/4 PASS.
- Local automated test suite: 32/32 PASS.
- Docker API security regression checks: 3/3 PASS.
- Total documented verification cases: 8/8 PASS.

The 32 pytest tests are reported separately and are not counted as 32 additional Docker test cases.

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

The following checks have not yet been fully documented for this deployment:

- Verify database persistence after container recreation.
- Test complete technician assignment and appointment creation workflows.
- Test invalid or expired authentication tokens.
- Verify role-specific access restrictions.
- Run dependency and Docker image vulnerability scans.
- Test simultaneous appointment requests for scheduling conflicts.

These checks should be completed before production deployment.

## 9. Conclusion

The SmartCRM L04 Docker deployment passed the documented build, accessibility, authentication, dashboard, and unauthorized-access checks.

The local automated test suite completed successfully with 32 passing tests.

All three previously identified BT3 authorization defects passed their unauthenticated-access regression tests against the Docker deployment.

The results support the use of this deployment for course-project demonstration. Additional security and operational testing is recommended before production use.
