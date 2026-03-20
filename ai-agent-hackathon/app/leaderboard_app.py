# ==========================================================
# 🏆 AI HACKATHON LEADERBOARD (ADMIN ONLY)
# ==========================================================
# ⚠️ IMPORTANT:
# Students SHOULD NOT modify this file
# This is used by the organizer to:
# - Run evaluation
# - View leaderboard
# - Check AI feedback

import streamlit as st
import pandas as pd
import os
import sys

# ==========================================================
# 🔧 FIX IMPORT PATH (VERY IMPORTANT)
# ==========================================================
# Ensures Streamlit can access evaluation module

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from evaluations.evaluate import run_all_evaluations, run_evaluation

# ==========================================================
# 📄 PAGE CONFIG
# ==========================================================
st.set_page_config(
    page_title="AI Hackathon Leaderboard",
    layout="wide"
)

st.title("🏆 AI Agent Hackathon Leaderboard")

# ==========================================================
# 🚀 RUN EVALUATION (ALL STUDENTS)
# ==========================================================
if st.button("🚀 Run Evaluation for All Students"):
    with st.spinner("Evaluating all student submissions..."):
        run_all_evaluations()
    st.success("✅ Evaluation Completed!")

# ==========================================================
# 📊 LOAD LEADERBOARD
# ==========================================================
leaderboard_path = "evaluations/leaderboard.csv"

st.subheader("🏅 Leaderboard Rankings")

if os.path.exists(leaderboard_path):
    leaderboard = pd.read_csv(leaderboard_path)

    if not leaderboard.empty:
        leaderboard = leaderboard.sort_values(by="score", ascending=False)

        # Show Top 3 separately (better UX)
        st.markdown("### 🥇 Top Performers")

        top3 = leaderboard.head(3)

        for i, row in top3.iterrows():
            st.write(f"**{row['student']}** — Score: {round(row['score'],4)}")

        st.markdown("---")

        st.dataframe(leaderboard, use_container_width=True)

    else:
        st.warning("⚠️ Leaderboard is empty. Run evaluation first.")

else:
    st.warning("⚠️ No leaderboard found. Click 'Run Evaluation' first.")

# ==========================================================
# 🧠 STUDENT FEEDBACK VIEWER
# ==========================================================
st.subheader("🧠 AI Feedback Viewer")

outputs_folder = "outputs"

if os.path.exists(outputs_folder):
    files = [f for f in os.listdir(outputs_folder) if f.endswith(".csv")]

    if files:
        student_file = st.selectbox("Select Student Submission", files)

        if st.button("🔍 Evaluate Selected Student"):

            student_name = student_file.replace("_predictions.csv", "")
            file_path = os.path.join(outputs_folder, student_file)

            result = run_evaluation(student_name, file_path)

            if "error" in result:
                st.error(result["error"])
            else:
                st.success(f"🏆 Score: {result['final_score']}")

                st.write("### 📊 Metrics")
                st.json(result["metrics"])

                st.write("### 🤖 AI Feedback")
                st.write(result["feedback"])

    else:
        st.info("📂 No student files found in outputs folder.")

else:
    st.warning("⚠️ Outputs folder not found.")

# ==========================================================
# ⚙️ SETTINGS (OPTIONAL)
# ==========================================================
st.sidebar.title("⚙️ Settings")

auto_refresh = st.sidebar.checkbox("Auto Refresh")

if auto_refresh:
    st.experimental_rerun()