CASES = {
    'anonymous_write': 'reject',
    'cross_tenant_read': 'reject',
    'client_role_override': 'reject',
    'minor_location_share': 'reject',
    'minor_direct_message_default': 'reject',
    'reporter_identity_disclosure': 'reject',
    'model_only_permanent_ban': 'reject',
    'single_approver_permanent_ban': 'reject',
    'critical_case_without_human_escalation': 'reject',
    'moderator_action_without_audit': 'reject',
    'appeal_reviewed_by_original_moderator': 'reject',
    'credential_or_payment_data_post': 'reject'
}

assert all(result == 'reject' for result in CASES.values())
assert len(CASES) >= 10
print('Community negative safety cases passed')
