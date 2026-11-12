# SmartCRM L04 – Deployment Guide

**Project:** SmartCRM – Technician Assignment and Appointment Management
**Student:** Nguyễn Ngọc Hiếu
**Student ID:** 2374802010142
**Review Date:** November 12, 2026
**Version:** 1.1 – BT3 Deployment Verification
**Repository:** https://github.com/Hieu2374802010142/smartcrm-2374802010142-technician-assignment

## 1. Overview

SmartCRM L04 is a web-based warranty management application developed using Python, FastAPI, and SQLite.

The application allows center managers to manage warranty tickets, assign technicians, and schedule delivery or pickup appointments. Authentication and role-based authorization protect management operations.

This guide explains how to install, configure, deploy, test, and troubleshoot the application using Docker Compose.

It also documents the fresh-clone deployment verification performed for BT3.

## 2. System Requirements

The following software is required:

- Docker Desktop with Docker Compose support
- Git
- A modern web browser, such as Google Chrome
- Python 3.12 and pytest (optional for local testing)

The application uses:

- **Backend:** Python 3.12, FastAPI, and Uvicorn
- **Frontend:** HTML, CSS, and JavaScript
- **Database:** SQLite
- **Containerization:** Docker and Docker Compose
- **API documentation:** OpenAPI and Swagger UI

Docker Desktop must be running before executing Docker Compose commands.

## 3. Installation and Setup

### Step 1: Clone the repository

Open Terminal and run:

```bash
git clone https://github.com/Hieu2374802010142/smartcrm-2374802010142-technician-assignment.git
```

Navigate to the project directory:

```bash
cd smartcrm-2374802010142-technician-assignment
```

For release verification, the project also provides the Git tag `v1.0.1`.

To inspect that release:

```bash
git checkout v1.0.1
```

This command may place Git in a detached HEAD state. Use a separate clone for release verification instead of changing the main development working copy.

### Step 2: Configure environment variables

Create a local `.env` file in the project root.

The application requires the following administrator authentication variables:

```env
SMARTCRM_ADMIN_USER=manager
SMARTCRM_ADMIN_PASSWORD_SALT=<generated-salt>
SMARTCRM_ADMIN_PASSWORD_HASH=<generated-password-hash>
```

The example values are placeholders and must not be used as real credentials.

Generate the password hash and salt using the project's administrator setup procedure.

The authentication implementation uses PBKDF2-HMAC-SHA256 with 600,000 iterations.

Do not store a plaintext password in `SMARTCRM_ADMIN_PASSWORD_HASH`.

The `.env` file contains sensitive configuration and must not be committed to GitHub.

The repository provides `.env.example` for configuration guidance.

Docker Compose reads the local `.env` file using its environment configuration.

### Step 3: Build and start the application

From the project directory, run:

```bash
docker compose up -d --build
```

This command builds the application image and starts the SmartCRM container.

The standard Compose configuration maps:

```text
127.0.0.1:8000 -> container port 8000
```

The application uses a persistent SQLite database stored in a Docker named volume.

### Step 4: Verify the running container

Check the service status:

```bash
docker compose ps
```

Inspect recent logs:

```bash
docker compose logs --tail=50
```

The expected result is a running, healthy SmartCRM container without startup errors.

Check application health:

```bash
curl -i http://127.0.0.1:8000/health
```

Expected successful response:

```json
{
  "status": "ok",
  "db": "up"
}
```

HTTP status `200` indicates that the application can access its SQLite database.

If the database check fails, the health endpoint returns HTTP `503` with a general error response.

## 4. Accessing the Application

After successful deployment, the following local URLs are available:

| Service | URL |
|---|---|
| SmartCRM Web Interface | http://127.0.0.1:8000/app |
| Swagger API Documentation | http://127.0.0.1:8000/docs |
| OpenAPI Specification | http://127.0.0.1:8000/openapi.json |
| Application Health Check | http://127.0.0.1:8000/health |
| SQLite Connection Test | http://127.0.0.1:8000/db-test |

Open the SmartCRM Web Interface and log in using the configured manager account.

After authentication, the manager can access the dashboard, technician management, warranty tickets, technician assignments, and appointment scheduling.

The backend includes 17 operations in its OpenAPI specification.

The frontend route `/app` is excluded from the OpenAPI schema.

## 5. Database Initialization and Persistence

SmartCRM uses SQLite as its application database.

The Docker configuration uses the following database path:

```text
/data/smartcrm.db
```

The database directory is mounted to the named Docker volume `smartcrm_data`.

The application's startup procedure initializes the database and performs seed operations as configured.

To stop the application without intentionally deleting the database volume:

```bash
docker compose down
```

To start it again:

```bash
docker compose up -d
```

**Important:** Do not run `docker compose down -v` unless you intentionally want to delete the associated Docker volumes and their stored data.

The Compose configuration is designed to preserve database data across container recreation. However, a separate end-to-end persistence test involving new records and container recreation has not been recorded as completed in the BT3 verification evidence.

## 6. Testing and Verification

### 6.1 Automated Testing

Run the automated test suite from the project directory:

```bash
python3 -m pytest -q
```

The latest verified main-repository test execution completed successfully:

```text
................................ [100%]
32 passed in 0.28s
```

The result confirms that all 32 tests in that execution passed.

The test suite includes functional validation and authentication-related regression checks.

### 6.2 Docker Deployment Verification

The following checks were completed during BT3 verification:

| Verification Item | Result |
|---|---|
| Docker image build | PASS |
| Docker container startup | PASS |
| Container health status | PASS |
| Application health endpoint | PASS |
| Frontend `/app` response | PASS |
| Manager login request | PASS |
| OpenAPI endpoint discovery | PASS |
| Automated test execution | PASS |

The standard deployment uses port `8000`.

The deployment was tested locally using Docker Desktop.

### 6.3 Fresh Clone Verification

A separate test directory was used to verify deployment from a fresh clone:

```text
~/workspace/smartcrm-bt3-fresh-clone
```

The release tag used for this verification was:

```text
v1.0.1
```

The fresh-clone environment used the standard Compose configuration together with a local port override file:

```text
compose.fresh.yaml
```

The override mapped host port `8001` to container port `8000`.

The verification command was:

```bash
docker compose -f compose.yaml -f compose.fresh.yaml up -d --build
```

To inspect the fresh-clone container:

```bash
docker compose -f compose.yaml -f compose.fresh.yaml ps
```

The following endpoints were successfully verified:

| Endpoint | Expected Result | Observed Result |
|---|---|---|
| `http://127.0.0.1:8001/health` | HTTP 200 | PASS |
| `http://127.0.0.1:8001/app` | HTTP 200 | PASS |
| `POST /api/auth/login` | HTTP 200 with valid credentials | PASS |

The health endpoint returned:

```json
{
  "status": "ok",
  "db": "up"
}
```

The fresh-clone container reported a healthy status.

**Note:** The `compose.fresh.yaml` file was used as a local verification override. It is not required for the standard deployment and should not be assumed to exist in every clone.

### 6.4 Authentication and Authorization Verification

The application requires manager authentication for technician and warranty management endpoints.

Regression verification confirmed that unauthenticated requests to the following endpoints return HTTP `401`:

- `GET /api/technicians`
- `GET /api/tickets/unassigned`
- `GET /api/tickets/assignments`

These protections correspond to the BT3 fixes BUG-03, BUG-02, and BUG-01.

Invalid login credentials return HTTP `401`.

Malformed login request data is rejected with HTTP `422`.

Role-based authorization checks are also included in the automated tests.

### 6.5 Manual Dashboard Verification

The following dashboard data was observed during verification:

- Three unassigned warranty tickets
- Three active technicians
- Zero active assignments in the tested database state

These values describe the observed test environment, not fixed application limits.

The complete technician assignment and appointment creation workflow should be tested separately when validating all user interactions.

## 7. Security Considerations

SmartCRM includes several security controls.

### 7.1 Authentication

Administrator credentials are verified using a salted PBKDF2-HMAC-SHA256 password hash.

The application issues bearer tokens for authenticated manager sessions.

Tokens are stored in application memory and expire after 60 minutes.

### 7.2 Authorization

Protected management routes require manager permission.

Unauthorized requests are rejected with HTTP `401`, while insufficient permissions can result in HTTP `403`.

### 7.3 Input Validation

Pydantic validates API request fields.

The application also checks business rules, including valid appointment time ranges and overlapping technician schedules.

SQL repository operations use parameterized queries for dynamic values.

### 7.4 Secrets and Docker Protection

The `.env` file is excluded from version control.

The `.dockerignore` configuration excludes sensitive and unnecessary development files from the Docker build context.

The standard Compose configuration binds the application port to the local host.

### 7.5 Dependency Audit

A Python dependency audit was completed during BT3.

The audit reported:

```text
No known vulnerabilities found
```

This result applies to the audited dependencies at the time of verification and does not guarantee that the application is free from all vulnerabilities.

The Docker image itself was not confirmed as having completed a separate image vulnerability scan.

### 7.6 Known Security Limitations

The current application is a course-project implementation and is not fully production-hardened.

Remaining considerations include:

- Login rate limiting
- Comprehensive sensitive-log verification
- Exhaustive exception-handling tests
- Concurrent appointment scheduling tests
- Docker image vulnerability scanning
- Persistent session management for multi-instance deployment

Additional details are documented in `docs/checklist-bao-mat.md`.

## 8. Troubleshooting

### 8.1 Docker container does not start

Check the logs:

```bash
docker compose logs --tail=100
```

Verify that Docker Desktop is running and that the required `.env` configuration is present.

### 8.2 Port 8000 is already in use

Another application or container may already be using the port.

On macOS, inspect the port:

```bash
lsof -nP -iTCP:8000 -sTCP:LISTEN
```

Stop the conflicting service if appropriate.

Do not terminate an unknown process without checking what it is.

### 8.3 Administrator login fails

Check the administrator environment variables and verify that the stored salt and password hash were generated correctly.

A missing or invalid administrator configuration may result in HTTP `503`.

Incorrect login credentials return HTTP `401`.

Do not print passwords or authentication tokens into logs when troubleshooting.

### 8.4 Dashboard authentication error

Confirm that the frontend sends a valid bearer token in protected API requests.

If the token has expired, log in again.

After modifying application code, rebuild the container:

```bash
docker compose up -d --build
```

Refresh the browser after the new container is running.

### 8.5 Database health check fails

Check:

```bash
curl -i http://127.0.0.1:8000/health
```

If the response is HTTP `503`, inspect the container logs and verify that the database directory is accessible.

Also verify that the configured database path matches the Docker volume mount.

### 8.6 Database data is missing

Check whether the expected Docker named volume is attached.

Verify the database path and whether a different Compose project created a separate volume.

Avoid deleting the volume while troubleshooting.

### 8.7 Fresh Clone uses a different port

The standard environment uses port `8000`.

The separate fresh-clone verification environment used port `8001`.

Use the appropriate URL and Compose configuration for the environment currently running.

## 9. Conclusion

SmartCRM L04 was successfully deployed and verified in a local Docker environment.

The verified functionality includes container startup, SQLite health checks, manager login, frontend access, protected management endpoints, and automated testing.

The latest automated test execution reported **32 passed and 0 failed**.

A separate fresh-clone deployment was also verified using release tag `v1.0.1` and host port `8001`.

The deployment configuration supports SQLite persistence through a named Docker volume, although complete persistence testing remains a separate verification task.

This guide provides the installation, verification, security, and troubleshooting information needed to reproduce the verified BT3 deployment environment.