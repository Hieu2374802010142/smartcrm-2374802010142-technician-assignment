# SMARTCRM L04 – SECURITY CHECKLIST

**Project:** SmartCRM – Technician Assignment and Appointment Management
**Student:** Nguyễn Ngọc Hiếu
**Student ID:** 2374802010142
**Review Date:** November 12, 2026
**Version:** 1.1 – BT3 Final Security Review
**Environment:** macOS, Python 3.12, FastAPI, SQLite, Docker Compose

## 1. Purpose

This document evaluates the security controls implemented in SmartCRM L04 as part of Assignment 3 (BT3).

The review focuses on seven security criteria: secret management, input validation and SQL injection prevention, data ownership, password hashing, error handling, sensitive logging, and dependency security.

The results are based on source code inspection, automated tests, Docker deployment verification, Git configuration checks, and dependency auditing.

**Status definitions:**

- **DONE:** The requirement has been verified within the documented scope.
- **NOT DONE:** The requirement is incomplete or has not been sufficiently verified.
- **N/A:** The requirement does not apply to the current system design.

## 2. Security Checklist

### SEC-01: Secrets and Git Repository Protection

**Requirement:** Prevent passwords, authentication secrets, and sensitive environment configuration from being committed to Git.

**Status: DONE**

**Implementation and evidence:**

- Administrator credentials are configured through environment variables.
- The local `.env` file is excluded from Git tracking.
- The `.dockerignore` file excludes `.env` and `.env.*`.
- The `.env.example` file is retained as a configuration template.
- The inspected Git history did not reveal a committed local `.env` file.
- Docker Compose loads environment configuration separately from application source code.

**Evidence files:**

- `.gitignore`
- `.dockerignore`
- `.env.example`
- `compose.yaml`

**Limitations:** This review does not constitute an exhaustive secret scan of every historical file or third-party dependency.

### SEC-02: Input Validation and SQL Injection Prevention

**Requirement:** Validate user input and prevent SQL injection vulnerabilities.

**Status: DONE**

**Implementation and evidence:**

- FastAPI and Pydantic validate API request data.
- Invalid request types are rejected with HTTP 422.
- Ticket and technician identifiers are validated.
- Appointment end times must be later than start times.
- Appointment scheduling checks for overlapping active appointments.
- Both repository modules use parameterized SQL queries with `?` placeholders for dynamic values.
- No direct concatenation of user-provided input into SQL statements was identified in the two reviewed repository files.
- SQLite transactions use `BEGIN IMMEDIATE` in important assignment and scheduling operations.

**Evidence files:**

- `src/backend/repositories/technician_repository.py`
- `src/backend/repositories/ticket_repository.py`
- `src/backend/routes/ticket_routes.py`
- `src/backend/routes/technician_routes.py`
- `src/backend/services/ticket_service.py`
- `docs/test-plan-bt3.md`
- `docs/test-report.md`

**Limitations:** The DONE status applies to the reviewed implementation. Exhaustive fuzz testing and concurrent-request testing have not been completed.

### SEC-03: Owner-Level Data Access Control

**Requirement:** Ensure users can access only data they own or are authorized to manage.

**Status: N/A**

**Reason:**

The current SmartCRM L04 implementation uses a manager-oriented administration model rather than separate customer accounts with individual data ownership.

The reviewed management APIs require the `manager` role.

Therefore, per-customer ownership checks are not applicable to the current implemented account model.

**Related security control:**

Backend authorization is enforced through `get_current_user()` and `require_manager()`.

**Evidence files:**

- `src/backend/auth/security.py`
- `src/backend/routes/ticket_routes.py`
- `src/backend/routes/technician_routes.py`

**Future consideration:** If customer or technician accounts are introduced, owner-level or role-specific data access rules must be implemented and tested.

### SEC-04: Password Hashing and Authentication

**Requirement:** Protect stored passwords and authenticate management users securely.

**Status: DONE**

**Implementation and evidence:**

- Administrator passwords are processed using PBKDF2-HMAC-SHA256.
- Password hashing uses 600,000 iterations and a salt.
- Authentication compares credential values using `hmac.compare_digest()`.
- The password hash and salt are loaded from environment variables.
- The setup script uses `getpass` for password input.
- Successful login returns a bearer token with the `manager` role.
- Tokens expire after 60 minutes.
- Invalid login credentials return HTTP 401.
- Protected management endpoints reject missing or invalid authentication tokens.

**Evidence files:**

- `src/backend/routes/auth_routes.py`
- `src/backend/auth/security.py`
- `src/backend/setup_admin.py`
- `docs/bug-log-bt3.md`

**Limitations:**

- Authentication tokens are stored in application memory.
- Sessions are lost when the application restarts.
- No login rate-limiting mechanism was identified during the review.
- Additional authentication hardening would be necessary for a public production deployment.

### SEC-05: Error Handling and Stack Trace Protection

**Requirement:** Avoid exposing internal stack traces, database details, or sensitive implementation information through API errors.

**Status: NOT DONE**

**Verified implementation:**

- No explicit `debug=True` configuration was found in the reviewed backend source.
- Authentication errors use fixed response messages.
- Ticket and technician services convert handled SQLite errors into general application error messages.
- The `/health` endpoint returns a generic HTTP 503 response when its database check fails.
- No direct `str(exc)` or traceback response was identified in the reviewed source.

**Remaining verification:**

- Test unexpected runtime exceptions against the deployed API.
- Verify that all unhandled errors return safe responses.
- Review the `/db-test` endpoint's behavior when the database is unavailable.

**Evidence files:**

- `src/backend/main.py`
- `src/backend/routes/auth_routes.py`
- `src/backend/routes/ticket_routes.py`
- `src/backend/routes/technician_routes.py`

**Reason for status:** Existing controls are present, but complete error-disclosure verification has not been performed.

### SEC-06: Sensitive Information in Application Logs

**Requirement:** Prevent passwords, authentication tokens, and other sensitive information from being written to logs.

**Status: NOT DONE**

**Verified implementation:**

- No direct logging of administrator passwords or authentication tokens was identified in the reviewed Python source.
- The seed script prints operation summaries and record counts.
- The administrator setup script does not print the entered password.
- Previous Docker log inspection did not reveal exposed authentication credentials.

**Remaining verification:**

- Review access logging under authenticated requests.
- Verify log behavior during unexpected exceptions.
- Confirm that request bodies and authorization headers are not exposed by production logging configuration.
- Review log retention and access restrictions before public deployment.

**Evidence files:**

- `src/backend/seed.py`
- `src/backend/setup_admin.py`
- `src/backend/migrate.py`
- `src/backend/routes/auth_routes.py`

**Reason for status:** Source inspection found no direct sensitive logging, but comprehensive runtime logging verification remains incomplete.

### SEC-07: Dependency Versioning and Vulnerability Audit

**Requirement:** Pin application dependencies and check them for known security vulnerabilities.

**Status: DONE**

**Implementation and evidence:**

- The `requirements.txt` file contains 15 pinned dependency entries.
- The dependency audit was executed using `pip-audit`.
- The audit returned: `No known vulnerabilities found`.
- The audit result was recorded as security evidence.

**Evidence files:**

- `requirements.txt`
- `docs/screenshots/Security_Dependency_Audit.png`

**Limitations:**

- Dependency audits reflect known vulnerabilities at the time of execution.
- The Docker base image has not been separately verified through a completed image vulnerability scan.
- Dependencies should be audited again before future releases.

## 3. Additional Authentication and Authorization Verification

Three major authorization defects were identified and fixed during BT3.

| Bug ID | Affected API | Fix Commit | Result |
|---|---|---|---|
| BUG-01 | `GET /api/tickets/assignments` | `c8c966d` | Fixed |
| BUG-02 | `GET /api/tickets/unassigned` | `b50ce78` | Fixed |
| BUG-03 | `GET /api/technicians` | `a4651d7` | Fixed |

Unauthenticated requests to these endpoints were subsequently verified to return HTTP 401.

The management routes use backend authorization checks rather than relying only on frontend restrictions.

**Evidence:**

- `docs/bug-log-bt3.md`
- `docs/screenshots/Bug01.png`
- `docs/screenshots/Bug02.png`
- `docs/screenshots/Bug03.png`

## 4. Automated Testing and Docker Deployment

The following verification results were recorded during BT3:

| Verification | Result |
|---|---|
| Automated pytest suite | 32 tests passed |
| Python syntax check | Passed |
| Docker Compose build | Successful |
| Docker container health | Healthy |
| Fresh Clone deployment | Successful |
| `GET /health` | HTTP 200 |
| `GET /app` | HTTP 200 |
| Administrator login | HTTP 200 with valid credentials |
| Invalid login | HTTP 401 |
| Invalid request data | HTTP 422 |
| Unauthenticated protected APIs | HTTP 401 |
| Dependency vulnerability audit | No known vulnerabilities found |

The standard Docker deployment uses localhost port 8000.

The separate Fresh Clone verification uses localhost port 8001 through a Docker Compose override file.

The Fresh Clone was used to verify that the application could be started independently from the release source.

**Evidence documents:**

- `docs/test-report.md`
- `docs/test-report-docker.md`
- `docs/bug-log-bt3.md`
- `docs/screenshots/`

## 5. Security Review Summary

| ID | Security Criterion | Status |
|---|---|---|
| SEC-01 | Secrets and Git repository protection | DONE |
| SEC-02 | Input validation and SQL injection prevention | DONE |
| SEC-03 | Owner-level data access control | N/A |
| SEC-04 | Password hashing and authentication | DONE |
| SEC-05 | Error handling and stack trace protection | NOT DONE |
| SEC-06 | Sensitive information in application logs | NOT DONE |
| SEC-07 | Dependency versioning and vulnerability audit | DONE |

**Summary:**

- 4 criteria: DONE
- 2 criteria: NOT DONE
- 1 criterion: N/A

The NOT DONE classifications identify areas where complete verification or additional hardening remains necessary. They do not mean that no protective measures have been implemented.

## 6. Known Risks and Recommendations

1. Implement or verify safe handling of unexpected application exceptions.
2. Complete runtime testing of sensitive information exposure in application logs.
3. Introduce login rate limiting for public-facing deployments.
4. Consider persistent session management if multiple application instances are required.
5. Perform a Docker image vulnerability scan.
6. Conduct concurrent-request tests for technician assignment and appointment scheduling.
7. Configure HTTPS, production network restrictions, and appropriate container privileges before internet-facing deployment.
8. Repeat dependency and security checks whenever the application is updated.

## 7. Conclusion

SmartCRM L04 implements important security controls, including administrator authentication, manager-level API authorization, password hashing, parameterized SQL queries, input validation, and environment-based secret configuration.

During BT3, three major authorization defects were fixed, 32 automated tests passed, and the Docker deployment and Fresh Clone were successfully verified.

The dependency audit found no known vulnerabilities at the time of testing.

The application has demonstrated its suitability for the verified local course-project environment. However, additional security testing and hardening are required before it can be considered production-ready.

This document records the security evidence and remaining limitations for the BT3 submission.