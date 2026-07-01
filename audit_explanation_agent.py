def generate_audit_report(incident):
    return {
        "summary": "CPU spike incident resolved using auto-scaling",
        "root_cause": incident["root_cause"]["root_cause"],
        "resolution": "Scaled service capacity",
        "preventive_action": "Enable load testing before deployments"
    }
