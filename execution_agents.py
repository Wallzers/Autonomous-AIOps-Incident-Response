def execute_actions(plan):
    actions = []

    for action in plan["action_plan"]:
        if action == "scale_service":
            actions.append({
                "action": action,
                "status": "success",
                "details": "Scaled service from 3 → 6 instances"
            })

        if action == "restart_service":
            actions.append({
                "action": action,
                "status": "success",
                "details": "Service restarted successfully"
            })

    return {
        "execution_status": "completed",
        "actions": actions
    }
