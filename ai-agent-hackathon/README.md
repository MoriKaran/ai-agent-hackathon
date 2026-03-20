**🚀 AI Agent Hackathon Platform**
**🎯 Objective**

**Welcome to the AI Agent Hackathon!**
-In this challenge, you will:
-Explore a real-world dataset
-Build features based on your understanding
-Train a machine learning model
-Create your own AI Agent (Streamlit app)
-Submit predictions
-Get evaluated automatically using metrics + AI judge

**🧠 Architecture Overview**
Dataset → Exploration → Feature Engineering → Model Training → Predictions
                                                               ↓
                                                      AI Agent (Streamlit)
                                                               ↓
                                                      Evaluation System
                                                               ↓
                                                         Leaderboard
**🏗️ Project Structure**

ai-agent-hackathon/
│
├── data/                    # Dataset (already provided)
├── notebooks/              # Step-by-step notebooks
├── models/                 # Saved model (model.pkl)
├── outputs/                # Your submission goes here
├── evaluations/            # Evaluation system
├── app/                    # Streamlit UI (Agent + Leaderboard)
├── README.md

**🧭 PHASE-WISE GUIDE**
🔹 **PHASE 1 — Data Exploration**

📘 Notebook: 01_data_exploration.ipynb

What you will do:

Understand dataset structure
Identify patterns
Analyze relationships
Choose your target variable

**🎯 Target Options:**

target_churn → Classification
target_fraud → Classification
target_revenue → Regression
**
🔹 **PHASE 2 — Feature Engineering****

📘 Notebook: 02_feature_engineering.ipynb

What you will do:

Clean data
Encode categorical variables
Create new features
💡 Examples:
activity_score
engagement_ratio
spend_per_transaction

👉 This is the most important phase
👉 Better features = better model

**🔹 PHASE 3 — Model Training**

📘 Notebook: 03_model_training.ipynb

What you will do:

Train ML models
Compare performance
Save best model

🤖 Models you can use:

Type	Models
Basic	Logistic Regression
Tree-based	Random Forest, Gradient Boosting
Advanced	XGBoost
Regression	Linear Regression

**🔹 PHASE 4 — Generate Predictions**

📘 Notebook: 04_generate_predictions.ipynb

What you will do:
Load model
Predict on test data
Save output

📤 FINAL OUTPUT FORMAT
actual,prediction
📁 Save your file as:
outputs/YOURNAME_predictions.csv

Example:

outputs/harshit_predictions.csv
🔹 PHASE 5 — Build AI Agent

📘 File: app/app.py

Run your agent:
streamlit run app.py
What your agent does:

Takes user input
Uses your trained model
Shows predictions
Displays confidence

🔹 PHASE 6 — Evaluation

📘 File: app/leaderboard.py

Run leaderboard:
streamlit run leaderboard.py
Click:

👉 Run Evaluation

🏆 Scoring System
For Classification:

Accuracy → 50%
F1 Score → 30%
AI Judge → 20%
For Regression:
MSE (lower better) → 60%
R² Score → 20%
AI Judge → 20%

**🤖 AI JUDGE (SPECIAL FEATURE)**

Your model is also evaluated by AI based on:

Prediction quality
Generalization
Business usability

**🏆 LEADERBOARD**

Automatically updated
Supports tie-breaking
Fair ranking system

⚠️ RULES

✅ Use any model
✅ Create your own features
✅ Customize your AI agent

❌ Not Allowed:

Changing output format
Incorrect file naming
Multiple submissions after deadline

**🧠 HOW TO USE CHATGPT (VERY IMPORTANT)**

You are encouraged to use ChatGPT to improve your solution.

🔥 Example Prompts
Feature Engineering:
Suggest 5 advanced features for churn prediction dataset
Model Selection:
Which model is best for classification with tabular data?
Hyperparameter Tuning:
How to improve RandomForest performance?
Debugging:
Why is my model overfitting?
Evaluation:
How to improve F1 score?
💡 Pro Tips

**Focus on feature engineering first**

Try multiple models
Check feature importance
Keep model simple but effective

****🎯 FINAL CHECKLIST**
Before submission:

✔ Model trained
✔ Predictions generated
✔ File saved in outputs/
✔ File name correct
✔ Columns correct

**🚀 FINAL GOAL**

Build an AI Agent that is:

✅ Accurate
✅ Intelligent
✅ User-friendly
✅ Business-ready

**🔥 GOOD LUCK

“Your model is your brain,
but your agent is your product.”

🚀 Go build something amazing!**
