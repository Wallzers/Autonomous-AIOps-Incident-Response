def determine_root_cause(incident):
    if incident["incident_type"] == "service_crash":
        return {
            "root_cause": "Service process crashed due to runtime failure",
            "confidence": 0.91,
            "evidence": [
                "Process terminated unexpectedly",
                "Health checks failed",
                "Connection refused errors"
            ]
        }

    return {
        "root_cause": "Traffic surge after recent deployment",
        "confidence": 0.84,
        "evidence": [
            "CPU spike occurred after deployment",
            "Latency and errors increased simultaneously"
        ]
    }
