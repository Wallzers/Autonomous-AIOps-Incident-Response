import json
import streamlit as st
from orchestrator.fsm_controller import IncidentFSM

st.set_page_config(
    page_title="Autonomous AIOps Incident Response",
    layout="wide"
)

st.title("🧠 Autonomous AIOps Incident Response")
st.caption("AI-powered incident detection, reasoning, and remediation")

# Load data
USE_SERVICE_CRASH = True  # toggle this

if USE_SERVICE_CRASH:
    with open("data/service_crash.log") as f:
        logs = f.read()
    with open("data/service_crash_metrics.json") as f:
        metrics = json.load(f)
else:
    with open("data/cpu_spike.log") as f:
        logs = f.read()
    with open("data/cpu_usage.json") as f:
        metrics = json.load(f)

with open("data/cpu_spike.log") as f:
    logs = f.read()

with open("data/cpu_usage.json") as f:
    metrics = json.load(f)

fsm = IncidentFSM()
result = fsm.handle_incident(logs, metrics)

# ─────────────────────────────
# INCIDENT SUMMARY (TOP CARD)
# ─────────────────────────────
st.subheader("🚨 Incident Summary")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Incident Type", result["analysis"]["incident_type"])

with col2:
    st.metric("Severity", result["analysis"]["severity"].upper())

with col3:
    st.metric("Service Affected", result["analysis"]["affected_service"])

st.divider()

# ─────────────────────────────
# SYMPTOMS
# ─────────────────────────────
st.subheader("📌 Observed Symptoms")
for s in result["analysis"]["symptoms"]:
    st.markdown(f"- ⚠️ {s}")

st.divider()

# ─────────────────────────────
# ROOT CAUSE
# ─────────────────────────────
st.subheader("🔍 Root Cause Analysis")

st.success(f"**Likely Cause:** {result['root_cause']['root_cause']}")
st.progress(result["root_cause"]["confidence"])

st.caption(
    f"Confidence Score: {int(result['root_cause']['confidence'] * 100)}%"
)

st.markdown("**Supporting Evidence:**")
for e in result["root_cause"]["evidence"]:
    st.markdown(f"- 🔎 {e}")

st.divider()

# ─────────────────────────────
# REMEDIATION PLAN
# ─────────────────────────────
st.subheader("🛠️ Proposed Remediation Plan")

for step in result["plan"]["action_plan"]:
    st.markdown(f"- ✅ {step.replace('_', ' ').title()}")

st.info(result["plan"]["reasoning"])

st.divider()

# ─────────────────────────────
# EXECUTION + HUMAN OVERSIGHT
# ─────────────────────────────
if result["status"] == "WAITING_FOR_APPROVAL":
    st.warning("⏸ Human approval required before execution")

    colA, colB = st.columns(2)

    with colA:
        if st.button("✅ Approve Remediation"):
            final = fsm.handle_incident(logs, metrics, human_approval=True)
            st.success("Remediation executed successfully")

            st.subheader("📊 Execution Result")
            for act in final["execution"]["actions"]:
                st.markdown(
                    f"- 🚀 **{act['action']}** → {act['details']}"
                )

            st.subheader("🧾 Audit Report")
            st.write(final["audit"]["summary"])
            st.markdown(f"**Preventive Action:** {final['audit']['preventive_action']}")

    with colB:
        if st.button("❌ Reject"):
            st.error("Remediation rejected by human operator")

else:
    st.success("✅ Incident auto-resolved")

    st.subheader("📊 Execution Result")
    for act in result["execution"]["actions"]:
        st.markdown(
            f"- 🚀 **{act['action']}** → {act['details']}"
        )

    st.subheader("🧾 Audit Summary")
    st.write(result["audit"]["summary"])
    st.markdown(f"**Preventive Action:** {result['audit']['preventive_action']}")
