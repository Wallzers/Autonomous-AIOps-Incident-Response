from agents.incident_analysis import analyze_incident
from agents.root_cause_agents import determine_root_cause
from agents.remidiation_planner import plan_remediation
from agents.execution_agents import execute_actions
from agents.audit_explanation_agent import generate_audit_report


class IncidentFSM:

    def handle_incident(self, logs, metrics, human_approval=False):
        print("\n--- INCIDENT DETECTED ---")

        analysis = analyze_incident(logs, metrics)
        root_cause = determine_root_cause(analysis)
        plan = plan_remediation(analysis, root_cause)

        # ⛔ Pause for human approval if required
        if plan["requires_human_approval"] and not human_approval:
            return {
                "status": "WAITING_FOR_APPROVAL",
                "analysis": analysis,
                "root_cause": root_cause,
                "plan": plan
            }

        execution = execute_actions(plan)
        audit = generate_audit_report({
            "analysis": analysis,
            "root_cause": root_cause,
            "execution": execution
        })

        return {
            "status": "DONE",
            "analysis": analysis,
            "root_cause": root_cause,
            "plan": plan,
            "execution": execution,
            "audit": audit
        }
