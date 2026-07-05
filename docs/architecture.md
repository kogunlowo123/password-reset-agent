# Password Reset Agent Architecture

Automated password reset agent that verifies user identity through multi-factor challenges, resets passwords across enterprise systems, enforces password policies, and securely communicates new credentials.

## Domain Tools

- **verify_identity**: Verify user identity through security questions or MFA
- **reset_password**: Reset password in the target system after identity verification
- **check_password_policy**: Validate a new password against organizational policy
- **unlock_account**: Unlock a locked account after too many failed attempts
- **audit_reset_history**: View password reset history for a user account