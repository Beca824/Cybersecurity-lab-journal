# TryHackMe Progress

A collection of notes and key takeaways from completed TryHackMe learning modules, covering Linux, Windows, networking, offensive security, defensive security, and cybersecurity fundamentals.


## Linux Fundamentals (Pt 1)

* **Task:** Run basic Linux commands and navigate the file system.
* **Commands:** `echo`, `whoami`, `ls`, `ls -a`, `ls -l`, `cd`, `cat`
* **Learned:** Basic Linux CLI usage, file-system navigation, and the use of command flags such as `-a` and `-l`.
* **Key takeaway:** Linux powers a large portion of modern servers and security infrastructure, making CLI proficiency an essential cybersecurity skill.


## Windows Fundamentals 1

* **Task:** Explore the Windows GUI, user accounts, and system tools.
* **Tools:** Task Manager (`Ctrl+Shift+Esc`), `lusrmgr.msc`, Control Panel
* **Discovered:** Windows 11 Pro supports BitLocker, the NTFS file system is commonly used by Windows, and the `tryhackmebilly` user account was present.
* **Key takeaway:** Understanding Windows user accounts, permissions, and User Account Control (UAC) is important for securing and assessing Windows systems.


## What is Networking?

* **Task:** Learn basic networking concepts and use `ping` to test connectivity.
* **Command:** `ping 8.8.8.8`
* **Learned:** IP addresses identify devices on a network, MAC addresses identify network interfaces at the data-link layer, and the Internet is essentially a "network of networks."
* **Key takeaway:** Understanding networking fundamentals is essential for cybersecurity because attacks, defenses, and system communication all rely on networks.


## Training Impact on Teams

* **Task:** Understand the impact of security training on teams and organizations.
* **Learned:** Security training can improve security awareness, reduce human error, strengthen incident reporting, and contribute to a stronger security culture.
* **Key takeaway:** People are an important part of an organization's security posture. Effective security awareness training can reduce risk and strengthen overall organizational defense.


## OWASP Top 10 2025: IAAA Failures

* **Task:** Learn how failures in the IAAA model relate to application security risks.
* **IAAA:** Identity, Authentication, Authorization, and Accountability.
* **Discovered:**

  * **A01: Broken Access Control** → Authorization failures can allow users to access resources or perform actions they should not have access to, including through vulnerabilities such as IDOR.
  * **A07: Authentication Failures** → Weak passwords, poor authentication controls, and missing rate limiting can allow attackers to compromise accounts.
  * **A09: Logging & Alerting Failures** → Insufficient logging and alerting can allow malicious activity to go undetected, weakening accountability.
* **Key takeaway:** Failures in identity, authentication, authorization, and accountability can create multiple security weaknesses within an application.


## OWASP Top 10 2025: Application Design Flaws

* **Task:** Learn how design-level security weaknesses can affect applications.
* **Discovered:**

  * **AS02: Security Misconfigurations** → Default credentials, unnecessary services, and exposed administrative interfaces can increase the attack surface.
  * **AS03: Software Supply Chain Failures** → Compromised or vulnerable dependencies can introduce security risks into an application.
  * **AS04: Cryptographic Failures** → Weak or improperly implemented cryptography can expose sensitive information.
  * **AS06: Insecure Design** → Flawed architecture or missing security controls can create vulnerabilities that cannot always be fixed simply by patching individual pieces of code.
* **Key takeaway:** Security needs to be considered during application design and architecture, rather than treated as something to add after development.


## Offensive Security Intro

* **Task:** Assess a simulated banking website for vulnerabilities.
* **Command:** `gobuster dir -u http://fakebank.thm -w wordlist.txt`
* **Discovered:** Directory enumeration revealed the hidden `/bank-transfer` page. An IDOR vulnerability was then exploited to transfer $2000.
* **Key takeaway:** Directory enumeration can expose hidden functionality, while access-control vulnerabilities such as IDOR can have serious real-world consequences.


## Defensive Security Intro

* **Task:** Learn the fundamentals of preventing, detecting, and responding to cyber threats.
* **Discovered:**

  * **Security Operations Center (SOC)** → monitors and investigates security events.
  * **Digital Forensics and Incident Response (DFIR)** → investigates security incidents and helps determine what happened.
  * **Threat Intelligence** → collects and analyzes information about threats and adversaries.
* **Key takeaway:** Offensive and defensive security complement each other. Understanding how attackers operate helps defenders build stronger detection and response capabilities.


## Search Skills

* **Task:** Learn advanced search techniques for security research and information gathering.
* **Operators:** `"exact phrase"`, `site:`, `-` (exclude), `filetype:`
* **Key takeaway:** Effective search techniques make research and information gathering faster and more efficient.


## Careers in Cyber

* **Task:** Explore different career paths within cybersecurity.
* **Roles Covered:** Security Analyst, Security Engineer, Incident Responder, Penetration Tester, and GRC.
* **Key takeaway:** Cybersecurity offers diverse career paths, and technical knowledge is only one part of the equation. Communication, problem-solving, and other soft skills are equally important.
