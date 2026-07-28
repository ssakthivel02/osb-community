# ADR 0001: Server-authoritative community safety

## Decision
The server owns tenant scope, account age category, guardian restrictions, moderation state, enforcement outcome, report visibility and appeal status.

Clients may request actions but cannot declare authoritative moderation or identity attributes.

## Consequences
Every write requires authenticated policy evaluation. Moderator actions require audited privileged authorisation. Permanent bans require dual approval. Critical safeguarding cases require human escalation. Public views expose only approved fields.
