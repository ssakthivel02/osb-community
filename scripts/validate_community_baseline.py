import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
community = json.loads((root / 'config/community-policy.json').read_text())
moderation = json.loads((root / 'config/moderation-policy.json').read_text())

assert community['apiPrefix'].startswith('/api/v1/')
assert community['authenticationRequired'] is True
assert community['tenantIsolationRequired'] is True
assert set(['en-GB', 'ta']).issubset(community['supportedLocales'])
assert community['minorProtection']['guardianControls'] is True
assert community['minorProtection']['directMessagingDefault'] == 'disabled'
assert community['minorProtection']['locationSharing'] == 'forbidden'
assert community['moderation']['humanEscalation'] is True
assert community['moderation']['appealsSupported'] is True
assert community['moderation']['dualApprovalForPermanentBan'] is True
assert community['abuseControls']['groomingRiskEscalation'] is True
assert community['privacy']['piiMinimisation'] is True
assert moderation['permanentBanRequiresDualApproval'] is True
assert moderation['modelOnlyPermanentEnforcementForbidden'] is True
print('Community baseline validation passed')
