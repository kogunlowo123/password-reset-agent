# Password Reset Agent

[![CI](https://github.com/kogunlowo123/password-reset-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/password-reset-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: IT Operations | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Automated password reset agent that verifies user identity through multi-factor challenges, resets passwords across enterprise systems, enforces password policies, and securely communicates new credentials.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `verify_identity` | Verify user identity through security questions or MFA |
| `reset_password` | Reset password in the target system after identity verification |
| `check_password_policy` | Validate a new password against organizational policy |
| `unlock_account` | Unlock a locked account after too many failed attempts |
| `audit_reset_history` | View password reset history for a user account |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/password/verify` | Verify identity |
| `POST` | `/api/v1/password/reset` | Reset password |
| `POST` | `/api/v1/password/validate` | Check password policy |
| `POST` | `/api/v1/password/unlock` | Unlock account |
| `GET` | `/api/v1/password/history` | Audit reset history |

## Features

- Identity Verification
- Password Reset
- Policy Enforcement
- Secure Delivery
- Audit Logging

## Integrations

- Active Directory
- Okta
- Azure Ad
- Duo Mfa
- Servicenow

## Architecture

```
password-reset-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── password_reset_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**Active Directory + Identity Provider + MFA**

---

Built as part of the Enterprise AI Agent Platform.
