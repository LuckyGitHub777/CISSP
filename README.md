# CISSP Study Guide

A structured CISSP study guide and cybersecurity leadership knowledge roadmap aligned to ISC2 official guidance and the eight CISSP domains.

## Purpose

This repository organizes CISSP knowledge into a practical leadership system for cybersecurity governance, risk management, architecture, operations, identity, testing, software security, and mission protection.

CISSP is not only about knowing security tools. CISSP is about making defensible security decisions.

## Official Source Standard

This repository is maintained as a CISSP study guide and cybersecurity leadership knowledge roadmap.

ISC2 official guidance is the authority for CISSP exam facts, domains, weights, experience requirements, and certification policy. Legacy CISSP books, notes, and study materials may support foundational learning, but they must be checked against ISC2 official guidance before being treated as exam-aligned.

This repository is optimized for:

- ISC2 CISSP domains
- AI-aware cybersecurity leadership
- Cloud, identity, software supply chain, and operational resilience
- Risk-based decision-making
- Ethical, defensive, and authorized security practice
- Clear source authority and public GitHub safety

## Core Doctrine

Risk before tools.  
Governance before implementation.  
Policy before procedure.  
Law before preference.  
Safety before convenience.  
Ownership before access.  
Classification before protection.  
Architecture before patchwork.  
Evidence before assurance.  
Recovery before panic.  
Ethics before advantage.  

## CISSP Exam Facts

Exam facts, domain weights, experience requirements, and certification policies should be verified directly through ISC2 official guidance for exam planning.

| Exam Item | Source-Governed Detail |
|---|---|
| Exam authority | ISC2 official guidance |
| Domain model | Eight CISSP domains |
| Delivery model | Computerized Adaptive Testing |
| Exam length | Listed in ISC2 official guidance |
| Item range | Listed in ISC2 official guidance |
| Passing standard | Listed in ISC2 official guidance |
| Experience requirement | Listed in ISC2 official guidance |

Official sources:

- [ISC2 CISSP Certification](https://www.isc2.org/certifications/cissp)
- [ISC2 CISSP Exam Outline](https://www.isc2.org/certifications/cissp/cissp-certification-exam-outline)
- [ISC2 CISSP Experience Requirements](https://www.isc2.org/certifications/cissp/cissp-experience-requirements)
- [ISC2 Exam Outlines](https://www.isc2.org/certifications/exam-outlines)

## Validation Rule

Exam facts and domain weights are sourced claims. For exam planning, verify them through ISC2 official guidance.

## CISSP Domains and Weights

Domain weights are exam claims and should be verified through ISC2 official guidance for exam planning.

| Domain | Weight |
|---:|---|
| 1 | Security and Risk Management, 16% |
| 2 | Asset Security, 10% |
| 3 | Security Architecture and Engineering, 13% |
| 4 | Communication and Network Security, 13% |
| 5 | Identity and Access Management, 13% |
| 6 | Security Assessment and Testing, 12% |
| 7 | Security Operations, 13% |
| 8 | Software Development Security, 10% |

## CISSP Mindset

A technician fixes a system.  
A CISSP protects the mission.

A technician asks:

```text
What tool fixes this?
```

A CISSP asks:

```text
What risk exists?
Who owns it?
What law applies?
What policy governs it?
What control reduces it?
What evidence proves it?
How does the organization continue operating?
```

## Experience Requirement

ISC2 official guidance governs CISSP experience requirements. Verify experience rules directly through ISC2 for exam planning, endorsement planning, or certification claims.

Source:

- [ISC2 CISSP Experience Requirements](https://www.isc2.org/certifications/cissp/cissp-experience-requirements)

## Source Authority Notice

This repository is aligned to ISC2 official guidance and the eight CISSP domains.

Legacy CISSP study materials, including older all-in-one study guides, may still be useful for foundational concepts such as risk management, access control, cryptography, security operations, business continuity, software security, and legal or compliance principles. However, legacy materials may reflect outdated exam structures, retired domain models, older technologies, older laws, or superseded exam formats.

This repository uses ISC2 official guidance as the authority for exam facts, domain weights, experience requirements, and certification guidance.

Always verify CISSP requirements directly through ISC2.

## AI-Aware CISSP Layer

AI is treated as a cross-domain cybersecurity issue, not as a separate CISSP domain.

For CISSP study, AI should be understood through governance, risk, architecture, identity, testing, operations, and software security.

| CISSP Domain | AI-Aware Focus |
|---|---|
| Domain 1 | AI governance, policy, ethics, legal duty, risk ownership, acceptable use |
| Domain 2 | AI data classification, training data sensitivity, privacy, retention, data leakage |
| Domain 3 | Secure AI architecture, model pipeline protection, adversarial robustness, secure deployment |
| Domain 4 | AI API exposure, secure data movement, network segmentation, service communication |
| Domain 5 | Non-human identities, AI agents, service accounts, least privilege, privileged automation |
| Domain 6 | AI red teaming, model testing, drift testing, validation evidence, control assurance |
| Domain 7 | AI monitoring, incident response, abuse detection, rollback, continuity, recovery |
| Domain 8 | AI-assisted coding, insecure generated code, dependency risk, secrets exposure, secure SDLC |

Rule: AI does not replace CISSP judgment. AI increases the need for CISSP judgment.

## Study Method

Use this method for every domain:

1. Define the domain in plain English.
2. Learn the official domain scope.
3. Memorize the core terms.
4. Understand how the terms connect.
5. Apply the concepts to realistic scenarios.
6. Think like a security leader, not a tool operator.
7. Review wrong answers deeply.
8. Convert weak areas into flashcards.
9. Retest until the answer logic becomes obvious.

## Wrong Answer Review Method

Every missed question should become a learning artifact.

```text
Question topic:
CISSP domain:
My chosen answer:
Correct answer:
Why my answer was wrong:
Why the correct answer was better:
CISSP principle involved:
Rule to remember:
Flashcard created:
```

## Repository Structure

```text
CISSP/
├── README.md
├── LICENSE
├── SECURITY.md
├── CONTRIBUTING.md
├── domains/
│   ├── domain-01-security-and-risk-management.md
│   ├── domain-02-asset-security.md
│   ├── domain-03-security-architecture-and-engineering.md
│   ├── domain-04-communication-and-network-security.md
│   ├── domain-05-identity-and-access-management.md
│   ├── domain-06-security-assessment-and-testing.md
│   ├── domain-07-security-operations.md
│   └── domain-08-software-development-security.md
├── quick-reference/
│   ├── exam-facts.md
│   ├── domain-weights.md
│   ├── acronyms.md
│   ├── formulas.md
│   ├── cryptography.md
│   ├── access-control.md
│   ├── incident-response.md
│   └── software-security.md
├── study-system/
│   ├── exam-mindset.md
│   ├── accelerated-study-path.md
│   ├── standard-study-path.md
│   ├── extended-study-path.md
│   ├── weak-domain-tracker.md
│   └── wrong-answer-review.md
├── flashcards/
│   ├── domain-01-flashcards.md
│   ├── domain-02-flashcards.md
│   ├── domain-03-flashcards.md
│   ├── domain-04-flashcards.md
│   ├── domain-05-flashcards.md
│   ├── domain-06-flashcards.md
│   ├── domain-07-flashcards.md
│   └── domain-08-flashcards.md
├── practice/
│   ├── manager-mindset-drills.md
│   ├── risk-decision-drills.md
│   ├── scenario-analysis.md
│   └── practice-question-review-template.md
└── references/
    ├── official-source-standard.md
    └── legacy-reference-policy.md
```

## Disclaimer

This repository is an independent study guide and cybersecurity knowledge roadmap. It is not affiliated with, endorsed by, or sponsored by ISC2. CISSP and ISC2 are trademarks of ISC2. Always verify exam requirements, domain weights, policies, and official guidance directly through ISC2.

## Copyright and Reference Policy

This repository contains original study notes, learning structure, and cybersecurity knowledge organization.

Do not upload copyrighted books, proprietary exam guides, paid training materials, copied question banks, or copyrighted practice questions into this repository.

Legacy materials may be used for private study and historical awareness, but public repo content should be original, summarized in fresh language, and verified against ISC2 official guidance.

## Responsible Use

All cybersecurity material in this repository is for legal, ethical, defensive, and educational use only.

## Final Doctrine

No ethics, no CISSP.  
No official source, no exam claim.  
No governance, no authority.  
No risk analysis, no decision.  
No data owner, no data protection.  
No identity lifecycle, no access control.  
No architecture, no resilience.  
No testing, no assurance.  
No logs, no investigation.  
No recovery, no continuity.  
No secure SDLC, no trusted software.  
No AI governance, no AI trust.  
No evidence, no claim.
