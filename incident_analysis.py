def analyze_incident(logs, metrics):
    incident = {
        "incident_type": None,
        "severity": "low",
        "affected_service": "payment-api",
        "symptoms": []
    }

    # ---- SERVICE CRASH DETECTION ----
    if "Process terminated" in logs or "Connection refused" in logs:
        incident["incident_type"] = "service_crash"
        incident["severity"] = "critical"
        incident["affected_service"] = "auth-service"
        incident["symptoms"].extend([
            "Service process stopped",
            "Health checks failing",
            "Requests rejected"
        ])
        return incident

    # ---- CPU SPIKE DETECTION ----
    if "CPU usage exceeded" in logs:
        incident["incident_type"] = "cpu_spike"
        incident["severity"] = "high"
        incident["symptoms"].append("High CPU usage")

    if "Response latency increased" in logs:
        incident["symptoms"].append("Increased latency")

    if "ERROR" in logs:
        incident["symptoms"].append("Rising error rate")

    return incident
