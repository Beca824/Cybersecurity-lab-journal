# OWASP Top 10 2025: Application Design Flaws

## Overview

Application security problems are not always caused by vulnerable code. Some vulnerabilities originate from decisions made during application design, configuration, architecture, or dependency management.

Understanding these weaknesses is important because fixing a design flaw after an application has been built can be significantly more difficult than considering security during the design stage.


## AS02: Security Misconfigurations

Security misconfigurations occur when an application, server, framework, or other component is configured insecurely.

### Examples

* Default credentials remaining enabled
* Unnecessary services being exposed
* Administrative interfaces being publicly accessible
* Debug features being enabled in production
* Incorrect security settings

### Why it matters

Even when application code is secure, an insecure configuration can expose functionality or information that attackers can exploit.

**Security principle:** Secure configuration should be part of deployment and system design, not an afterthought.


## AS03: Software Supply Chain Failures

Modern applications often depend on external libraries, frameworks, packages, APIs, and other third-party components.

A software supply chain failure occurs when weaknesses or compromises within these dependencies introduce risks into an application.

### Examples

* Vulnerable third-party libraries
* Compromised dependencies
* Untrusted packages
* Poor dependency management
* Failure to monitor or update dependencies

### Why it matters

An application can contain secure code while still becoming vulnerable through a compromised or vulnerable dependency.

This demonstrates that application security extends beyond code written by the development team.


## AS04: Cryptographic Failures

Cryptographic failures occur when sensitive information is not adequately protected through appropriate cryptographic controls.

### Examples

* Weak encryption algorithms
* Improper cryptographic implementations
* Insecure storage of sensitive data
* Poor key management
* Transmitting sensitive information without adequate protection

### Why it matters

Sensitive information such as passwords, personal data, authentication tokens, or financial information can be exposed if cryptographic protections are weak or incorrectly implemented.

**Security principle:** Sensitive data should be protected both at rest and in transit using appropriate cryptographic mechanisms.


## AS06: Insecure Design

Insecure design occurs when an application's architecture or business logic does not adequately account for security requirements.

Unlike a simple coding mistake, an insecure design can represent a fundamental weakness in how the application is intended to operate.

### Examples

* Missing authorization requirements
* Unsafe business logic
* Lack of abuse-case analysis
* Security controls that were never included in the original design
* Trusting user-controlled input or actions without appropriate validation

### Why it matters

A vulnerability caused by insecure design may require changes to the application's architecture or business logic rather than simply changing one line of code.


## Why Design Matters

Security should be considered throughout the application lifecycle:

```text
Requirements
     ↓
Secure Design
     ↓
Development
     ↓
Testing
     ↓
Deployment
     ↓
Monitoring & Maintenance
```

If security is ignored during the design stage, vulnerabilities can become deeply embedded in the application.

For example:

```text
Insecure Design
      ↓
Weak Security Controls
      ↓
Vulnerable Implementation
      ↓
Exploitation
```

Trying to fix these issues only after deployment can be more expensive and difficult than designing the application securely from the beginning.


## Key Takeaways

* Security is not only a coding problem.
* Misconfigurations can expose otherwise secure applications.
* Third-party dependencies can introduce vulnerabilities into an application.
* Cryptographic controls must be implemented correctly to protect sensitive information.
* Insecure design can create vulnerabilities at an architectural or business-logic level.
* Security should be integrated into the application lifecycle from the design stage.
* **Secure by design is better than secure by patching.**
