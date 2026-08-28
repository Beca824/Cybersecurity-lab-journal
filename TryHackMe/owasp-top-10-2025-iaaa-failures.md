# OWASP Top 10 2025: IAAA Failures

## Overview

The IAAA model represents four important security functions within an application:

* **Identification** — Establishing who a user or entity claims to be.
* **Authentication** — Verifying that claimed identity.
* **Authorization** — Determining what an authenticated user is allowed to access or do.
* **Accountability** — Tracking and recording actions so that activity can be monitored and investigated.

Failures in these areas can create vulnerabilities that allow attackers to gain unauthorized access, perform actions they should not be able to perform, or operate without being detected.

---

## A01: Broken Access Control

**IAAA area affected:** Authorization

Broken Access Control occurs when an application does not properly enforce what authenticated users are permitted to access or perform.

### Example: IDOR

An **Insecure Direct Object Reference (IDOR)** occurs when an application uses a user-controlled identifier to access an object without properly checking whether the user is authorized to access it.

For example:

```text
/account?id=1001
```

If changing the identifier to:

```text
/account?id=1002
```

allows a user to view another person's account, the application has failed to properly enforce authorization.

### Why it matters

Authentication only establishes *who* a user is. Authorization determines *what that user can do*.

Therefore, an application can have strong authentication while still being vulnerable to broken access control.

---

## A07: Authentication Failures

**IAAA area affected:** Authentication

Authentication failures occur when an application does not adequately verify the identity of users.

Examples include:

* Weak or easily guessable passwords
* Missing rate limiting
* Poor password policies
* Inadequate authentication controls
* Improper session management

### Why it matters

If authentication controls are weak, attackers may be able to compromise legitimate accounts and then operate with the privileges of those users.

This demonstrates the relationship between the IAAA components: a failure in authentication can eventually lead to authorization problems if an attacker gains access to another user's account.

---

## A09: Logging & Alerting Failures

**IAAA area affected:** Accountability

Logging and alerting allow organizations to record activity and identify suspicious or malicious behavior.

A system with inadequate logging may fail to record important security events, while inadequate alerting can prevent security teams from responding to suspicious activity.

Examples include:

* Missing authentication logs
* Insufficient monitoring of privileged actions
* Failure to detect repeated failed login attempts
* Lack of alerts for suspicious activity
* Logs that do not contain enough information for investigation

### Why it matters

Without effective accountability, an organization may know that something went wrong but be unable to determine:

* What happened
* When it happened
* Which account was involved
* What actions were performed
* How the attacker gained access

---

## Relationship Between IAAA and Application Security

The IAAA model demonstrates that application security controls are interconnected.

A simplified attack path could look like:

```text
Authentication Failure
        ↓
Attacker gains access to an account
        ↓
Broken Access Control
        ↓
Unauthorized actions or data access
        ↓
Logging & Alerting Failure
        ↓
Attack remains undetected
```

A weakness in one area can therefore contribute to failures in another.


## Key Takeaways

* Authentication answers **"Who are you?"**
* Authorization answers **"What are you allowed to do?"**
* Accountability answers **"What did you do, and can we trace it?"**
* Strong authentication does not automatically mean strong authorization.
* Logging and alerting are essential for detecting and investigating security incidents.
* Application security requires multiple controls working together rather than relying on a single security mechanism.
