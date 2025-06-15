# HIPAA Compliance & Security Plan  
**Project: AI-on-FHIR – Natural Language Health Query System**

## 🔒 Overview
This application processes patient health-related queries using AI and returns simulated FHIR (Fast Healthcare Interoperability Resources) data. 
While it does not process real PHI (Protected Health Information), the system is designed with HIPAA compliance principles in mind for future 
real-world integration.

---

## 🔑 1. Authentication & Authorization

- **OAuth 2.0 / SMART on FHIR**  
  The application is designed to integrate with SMART on FHIR for secure, standardized access to FHIR APIs using OAuth 2.0.
  
- **Token-based Access**  
  All API requests would require access tokens to ensure users are authenticated and scoped to the correct level of data access.

---

## 🛡️ 2. Data Privacy & Encryption

- **In-Transit Encryption**  
  All communication (frontend → backend, backend → FHIR server) uses HTTPS (TLS 1.2+).

- **At-Rest Encryption**  
  If any sensitive data is stored (e.g., logs or temporary files), it will be encrypted using AES-256.

- **No PHI Storage**  
  The current version uses only simulated data. If real patient data is used, a strict no-caching policy will apply.

---

## 📜 3. Audit Logging

- **Request Tracing**  
  Each query and response will be logged with timestamps, user IDs (if available), and access scopes.

- **Anomaly Monitoring**  
  Logs can be integrated with tools like ELK Stack or CloudWatch for anomaly detection and alerting.

---

## 👥 4. Role-Based Access Control (RBAC)

- **Defined Roles**  
  - `Admin`: full access
  - `Clinician`: access to patients in their care
  - `Patient`: access to personal data only

- **Fine-Grained Access**  
  Backend enforces resource-level permissions, ensuring users can only access data they are authorized to view.

---

## ✅ Summary

The system is designed with HIPAA-compliant architecture in mind, including:
- OAuth 2.0 authentication
- TLS & encryption
- No PHI persistence
- Logging and RBAC enforcement

These principles ensure readiness for real-world healthcare integration with FHIR-based APIs.


