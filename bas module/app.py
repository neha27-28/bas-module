import streamlit as st
from attack_scenarios import SCENARIOS
from log_generator import generate_logs
from breach_narrator import narrate_breach
from anomaly_detector import AnomalyDetector

# Streamlit Page Configuration
st.set_page_config(page_title="AI Breach Simulator", layout="wide")
st.title("AI-Enhanced Breach and Attack Simulator")

# Scenario Selection
scenario = st.selectbox("Choose a breach scenario:", list(SCENARIOS.keys()))

if st.button("Simulate Attack"):
    events = SCENARIOS[scenario]
    
    # Generate synthetic logs with MITRE tactic mapping
    logs = generate_logs(events)

    # Display Logs with MITRE Tactic Mapping
    st.subheader("Generated Logs (with MITRE tactics)")
    st.dataframe(logs, use_container_width=True)

    # AI-generated Attack Narrative
    st.subheader("AI Attack Narrative")
    story = narrate_breach(events)
    st.write(story)

    # Anomaly Detection
    st.subheader("Anomaly Detection")
    detector = AnomalyDetector()
    detector.train(logs)
    annotated_logs = detector.predict(logs)

    # Display Anomalous Logs with Detection Results
    st.dataframe(annotated_logs, use_container_width=True)
