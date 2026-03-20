🚀 Git Submission Guide (For Students)
🎯 Objective

This guide will help you:
Clone the project
Work on notebooks
Submit your final output correctly
Push ONLY your prediction file

STEP 1 — Clone the Repository
🔹 Option 1 — Using Codespaces (Recommended)

👉 Open the GitHub repository
👉 Click:
Code → Codespaces → Create Codespace

Open terminal:

git clone https://github.com/YOUR-REPO-LINK.git
cd ai-agent-hackathon
🔄 STEP 2 — Always Pull Latest Code

Before starting work, run:

git pull origin main
👉 This ensures:
You have latest updates
No conflicts later

🧠 STEP 3 — Work on Notebooks
Follow instructions in:
notebooks/
👉 Steps:

Explore data
Clean data
Create features
Train model
Generate predictions

📤 STEP 4 — Save Your Output File

After final notebook:
👉 Save file in:

outputs/YOURNAME_predictions.csv
✅ Example:
outputs/harshit_predictions.csv
🚨 IMPORTANT RULE

Your file MUST:
Be inside outputs/
End with _predictions.csv
Contain columns: actual,prediction

🚀 STEP 5 — Push ONLY Your Output File
❗ DO NOT USE:
git add .

👉 This will push everything ❌

✅ USE THIS (VERY IMPORTANT)
git add outputs/YOURNAME_predictions.csv
git commit -m "Final submission - YOURNAME"
git push origin main


🔁 STEP 6 — Create Pull Request (PR)

After pushing:
👉 Go to GitHub (browser)
You will see:
“Compare & pull request”
Click:
👉 Create Pull Request

🧠 STEP 7 — Wait for Approval
👉 Organiser will:
Review your file
Merge if correct
🚨 IMPORTANT RULES
❌ DO NOT:

Modify notebooks
Modify app files
Modify evaluation code
Push entire project

✅ ONLY SUBMIT:
outputs/YOURNAME_predictions.csv
⚠️ INVALID SUBMISSION IF:

Multiple files in PR
Wrong file name
Wrong folder
Missing columns

💡 PRO TIPS
🔹 Check before pushing:
git status
👉 You should ONLY see:
outputs/YOURNAME_predictions.csv
🔹 If you added wrong files:
git reset

Then add again correctly.

🎯 FINAL CHECKLIST

Before submission:
✔ File exists in outputs/
✔ File name correct
✔ Only 1 file staged
✔ PR created