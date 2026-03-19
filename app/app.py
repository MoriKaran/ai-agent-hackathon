import streamlit as st
import pickle
import os
import pandas as pd

# ==========================================================
#  STEP 1 — AGENT NAME
# ==========================================================

st.set_page_config(page_title="AI Agent", layout="centered")

st.title("harshit - AI AGENT")  
st.write("Enter details below to get prediction")

# ==========================================================
#  STEP 2 — LOAD MODEL + FEATURES
# ==========================================================

MODEL_PATH = "models/model.pkl"
FEATURE_PATH = "models/features.pkl"

if not os.path.exists(MODEL_PATH):
    st.error(" Model not found. Please train your model first.")
    st.stop()

if not os.path.exists(FEATURE_PATH):
    st.error(" features.pkl not found. Please run training notebook.")
    st.stop()

# Load model
with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

# Load feature columns
with open(FEATURE_PATH, "rb") as f:
    feature_columns = pickle.load(f)

# ==========================================================
#  STEP 3 — INPUT FEATURES (DO NOT CHANGE)
# ==========================================================

st.subheader(" Input Features")

age = st.number_input("Age", min_value=18, max_value=80, value=30)  
monthly_spend = st.number_input("Monthly Spend (£)", value=100.0)  
num_transactions = st.number_input("Number of Transactions", value=10)  
tenure = st.number_input("Tenure (months)", value=12)  
last_login = st.number_input("Days Since Last Login", value=5)

# ==========================================================
#  STEP 4 — PREDICT BUTTON
# ==========================================================

if st.button(" Predict"):

    try:
        # ==================================================
        #  AUTO FEATURE ALIGNMENT (KEY FIX)
        # ==================================================

        input_df = pd.DataFrame(columns=feature_columns)
        input_df.loc[0] = 0

        # Base features
        if "age" in input_df.columns:
            input_df["age"] = age

        if "monthly_spend" in input_df.columns:
            input_df["monthly_spend"] = monthly_spend

        if "num_transactions" in input_df.columns:
            input_df["num_transactions"] = num_transactions

        if "tenure_months" in input_df.columns:
            input_df["tenure_months"] = tenure

        if "last_login_days" in input_df.columns:
            input_df["last_login_days"] = last_login

        # ==================================================
        #  FEATURE ENGINEERING (MATCH TRAINING)
        # ==================================================

        if "spend_per_transaction" in input_df.columns:
            input_df["spend_per_transaction"] = monthly_spend / (num_transactions + 1)

        if "activity_score" in input_df.columns:
            input_df["activity_score"] = num_transactions / (tenure + 1)

        if "engagement_ratio" in input_df.columns:
            input_df["engagement_ratio"] = last_login / (tenure + 1)

        if "high_spender_flag" in input_df.columns:
            input_df["high_spender_flag"] = int(monthly_spend > 100)

        if "frequent_user_flag" in input_df.columns:
            input_df["frequent_user_flag"] = int(num_transactions > 10)

        if "customer_value_score" in input_df.columns:
            input_df["customer_value_score"] = (monthly_spend * num_transactions) / (tenure + 1)

        # Fill missing columns
        input_df = input_df.fillna(0)

        # ==================================================
        #  STEP 5 — MODEL PREDICTION
        # ==================================================

        prediction = model.predict(input_df)

        # ==================================================
        #  STEP 6 — OUTPUT
        # ==================================================

        st.success(f"Prediction: {prediction[0]}")

        if prediction[0] == 1:
            st.error(" High Risk / Negative Outcome")
        else:
            st.success(" Positive Outcome")

        # ==================================================
        #  CONFIDENCE SCORE
        # ==================================================

        try:
            prob = model.predict_proba(input_df)[0][1]
            confidence = round(prob * 100, 2)
            st.info(f"Confidence: {confidence}%")
        except:
            st.warning(" Confidence not available")

    except Exception as e:
        st.error(" Prediction failed. Check feature alignment.")
        st.text(str(e))