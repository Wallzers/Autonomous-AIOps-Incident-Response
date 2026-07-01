def plan_remediation(incident, root_cause):

    if incident["incident_type"] == "service_crash":
        return {
            "action_plan": [
                "restart_service",
                "verify_health_checks"
            ],
            "requires_human_approval": True,
            "reasoning": "Service restart may impact users and requires approval"
        }

    return {
        "action_plan": [
            "scale_service",
            "monitor_metrics"
        ],
        "requires_human_approval": False,
        "reasoning": "Auto-scaling is safe for traffic surges"
    }
