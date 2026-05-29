import streamlit as st
import re
from utils.storage import save_assessment
from utils.report_generator import generate_report

from services.gemma_service import ask_gemma

st.set_page_config(
    page_title="MindPulse AI",
    page_icon="🧠",
    layout="wide"
)

# Header
st.title("🧠 MindPulse AI")

st.info(
    "This tool provides wellness guidance and is not a substitute for professional medical advice."
)

st.subheader("Mental Wellness Assistant powered by Gemma 4")

# Sidebar
with st.sidebar:
    st.header("Features")

    st.success("Stress Detection")
    st.success("Anxiety Assessment")
    st.success("Burnout Analysis")
    st.success("Privacy First")

    st.markdown("---")

    st.write(
        "Powered by Gemma 4 running locally via Ollama."
    )

    st.markdown("---")

    st.info(
        "🔒 Privacy First\n\nYour data never leaves your machine."
    )

# Mood Selector
mood = st.selectbox(
    "Select your current mood",
    [
        "😊 Happy",
        "😔 Sad",
        "😰 Anxious",
        "😡 Angry",
        "😴 Tired"
    ]
)

# User Input
user_input = st.text_area(
    "How are you feeling today?",
    height=150
)

# Analyze Button
if st.button("Analyze"):

    if not user_input.strip():
        st.warning("Please enter your thoughts.")
        st.stop()

    # Simple safety guardrail
    danger_keywords = [
        "suicide",
        "kill myself",
        "end my life",
        "want to die",
        "self harm",
        "don't want to live anymore"
    ]

    if any(word in user_input.lower() for word in danger_keywords):
        st.error(
            "⚠️ Please contact a trusted person, family member, or mental health professional immediately."
        )
        st.stop()

    with st.spinner("Analyzing with Gemma..."):

        prompt = f"""
You are a mental wellness assistant.

Current Mood Selected:
{mood}

User Message:
{user_input}

Consider BOTH the selected mood and the written message.

If the mood and message conflict, mention the inconsistency.

Return EXACTLY in this format:

Stress Score: X/10
Anxiety Score: X/10
Burnout Score: X/10

Mood Observation:
<observation>

Summary:
<summary>

Recommendations:
- item 1
- item 2
- item 3

Keep the response concise.
"""

        result = ask_gemma(prompt)

    st.success("Analysis Complete")

    stress = re.search(r"Stress Score:\s*(\d+\/10)", result)
    anxiety = re.search(r"Anxiety Score:\s*(\d+\/10)", result)
    burnout = re.search(r"Burnout Score:\s*(\d+\/10)", result)

    if stress and anxiety and burnout:

        stress_score = stress.group(1).replace("/10", "")
        anxiety_score = anxiety.group(1).replace("/10", "")
        burnout_score = burnout.group(1).replace("/10", "")

        # Save to CSV
        save_assessment(
            mood,
            stress_score,
            anxiety_score,
            burnout_score
        )

        col1, col2, col3 = st.columns(3)

        col1.metric("Stress", stress.group(1))
        col2.metric("Anxiety", anxiety.group(1))
        col3.metric("Burnout", burnout.group(1))

        st.divider()

        st.write(f"**Selected Mood:** {mood}")

        st.markdown(result)

        # Generate PDF
        pdf_file = generate_report(
            mood,
            result
        )

        with open(pdf_file, "rb") as file:

            st.download_button(
                label="📄 Download Wellness Report",
                data=file,
                file_name="MindPulse_Report.pdf",
                mime="application/pdf"
            )