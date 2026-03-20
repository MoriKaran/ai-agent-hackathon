import streamlit as st
import pandas as pd
import os

# -----------------------------------
# Page Config
# -----------------------------------
st.set_page_config(
    page_title="Hackathon Question Portal",
    page_icon="🎯",
    layout="centered"
)

# -----------------------------------
# Load Data (Robust Version)
# -----------------------------------
@st.cache_data
def load_data():
    try:
        # Get project root directory
        BASE_DIR = os.path.dirname(os.path.dirname(__file__))
        file_path = os.path.join(BASE_DIR, "students_question.csv")

        # Check if file exists
        if not os.path.exists(file_path):
            st.error("❌ students_question.csv file not found in project root")
            st.stop()

        # Read CSV (no header)
        df = pd.read_csv(file_path, header=None)

        # Validate structure
        if df.shape[1] < 2:
            st.error("❌ CSV format incorrect. Must have 2 columns: email, question")
            st.stop()

        # Assign column names
        df = df.iloc[:, :2]
        df.columns = ["email", "question"]

        # Clean data
        df["email"] = df["email"].astype(str).str.strip().str.lower()
        df["question"] = df["question"].astype(str).str.strip()

        return df

    except Exception as e:
        st.error(f"❌ Error loading CSV: {e}")
        st.stop()


df = load_data()

# -----------------------------------
# UI
# -----------------------------------
st.title("🎯 AI Hackathon Question Portal")

st.markdown("""
Welcome!  
Enter your registered email to get your assigned question.
""")

st.markdown("---")

# Input
email = st.text_input("📧 Enter your email").strip().lower()

# Button
if st.button("Get My Question"):

    if email == "":
        st.warning("⚠️ Please enter your email")

    else:
        result = df[df["email"] == email]

        if not result.empty:
            question = result["question"].values[0]

            st.success("✅ Question Assigned Successfully")

            st.markdown("---")

            st.write(f"👤 Logged in as: **{email}**")

            st.markdown(f"""
            ### 📌 Your Question:
            **{question}**
            """)

            st.info("💡 Tip: Copy this question and use it in your notebook")

        else:
            st.error("❌ Email not found. Please contact organizer.")

# -----------------------------------
# Footer
# -----------------------------------
st.markdown("---")
st.caption("🚀 Powered by AI Hackathon Platform")