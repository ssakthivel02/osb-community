# Community Threat Model

## Protected assets
User identity, tenant boundaries, minor safety, moderation evidence, private messages, reports and appeals.

## Principal threats
- Cross-tenant data exposure
- Grooming and coercive contact
- Harassment, hate and credible threats
- Spam, scams and malicious links
- Moderator privilege abuse
- False reporting and brigading
- PII leakage through posts, logs or exports
- Automated moderation overreach
- Appeal tampering and evidence deletion

## Required controls
Authenticated and authorised APIs, tenant-derived scope, child-safe defaults, rate limiting, link controls, immutable moderation audit, human escalation, independent appeals, dual approval for permanent bans, PII minimisation and incident response.

## Trust boundary
Clients are untrusted. User-supplied tenant, age, role, moderation state and enforcement outcome must never be authoritative.
