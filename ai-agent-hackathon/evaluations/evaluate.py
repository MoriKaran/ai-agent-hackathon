import pandas as pd
import json
import os
import re
from evaluations.metrics import calculate_metrics
from evaluations.ai_judge import evaluate_with_ai


# ==========================================================
# 🔍 Extract JSON from AI response
# ==========================================================
def extract_json(text):
    try:
        match = re.search(r'\{.*\}', text, re.DOTALL)
        if match:
            return json.loads(match.group())
        else:
            raise ValueError("No JSON found in AI response")
    except Exception as e:
        return {
            "score": 0,
            "feedback": f"AI parsing failed: {str(e)}"
        }


# ==========================================================
# 🧠 Main Evaluation Function
# ==========================================================
def run_evaluation(student_name, file_path):

    print(f"\n🔍 Evaluating: {student_name}")

    # -------------------------------
    # Step 1: Load file
    # -------------------------------
    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        return {
            "student": student_name,
            "error": f"File read error: {str(e)}"
        }

    # -------------------------------
    # Step 2: Validate columns
    # -------------------------------
    required_cols = ["actual", "prediction"]

    if not all(col in df.columns for col in required_cols):
        return {
            "student": student_name,
            "error": "Missing required columns: actual, prediction"
        }

    if len(df) == 0:
        return {
            "student": student_name,
            "error": "Empty prediction file"
        }

    y_true = df["actual"]
    y_pred = df["prediction"]

    # -------------------------------
    # Step 3: Calculate metrics
    # -------------------------------
    try:
        metrics = calculate_metrics(y_true, y_pred)
    except Exception as e:
        return {
            "student": student_name,
            "error": f"Metric calculation failed: {str(e)}"
        }

    # -------------------------------
    # Step 4: AI Evaluation
    # -------------------------------
    sample_predictions = df.head(10).to_dict(orient="records")

    try:
        ai_raw = evaluate_with_ai(metrics, sample_predictions)
        ai_result = extract_json(ai_raw)
    except Exception as e:
        ai_result = {
            "score": 0,
            "feedback": f"AI evaluation failed: {str(e)}"
        }

    # -------------------------------
    # Step 5: Normalize AI score
    # -------------------------------
    ai_score = ai_result.get("score", 0)
    ai_score_normalized = ai_score / 10  # 0–10 → 0–1

    # -------------------------------
    # Step 6: Final Score Calculation
    # -------------------------------
    problem_type = metrics.get("problem_type", "classification")

    if problem_type == "classification":
        final_score = (
            metrics.get("accuracy", 0) * 0.5 +
            metrics.get("f1_score", 0) * 0.3 +
            ai_score_normalized * 0.2
        )
    else:  # regression
        final_score = (
            (1 / (1 + metrics.get("mse", 1))) * 0.6 +
            metrics.get("r2_score", 0) * 0.2 +
            ai_score_normalized * 0.2
        )

    result = {
        "student": student_name,
        "metrics": metrics,
        "ai_score": ai_score,
        "feedback": ai_result.get("feedback", ""),
        "final_score": round(final_score, 4),
        "problem_type": problem_type
    }

    print(f"✅ Score for {student_name}: {result['final_score']}")

    return result


# ==========================================================
# 🏆 Leaderboard Update Function
# ==========================================================
def update_leaderboard(result):

    if "error" in result:
        print(f"❌ Skipping {result['student']} due to error: {result['error']}")
        return

    path = "evaluations/leaderboard.csv"

    # -------------------------------
    # Load or create leaderboard
    # -------------------------------
    if os.path.exists(path):
        leaderboard = pd.read_csv(path)
    else:
        leaderboard = pd.DataFrame(columns=[
            "student", "score", "accuracy", "f1_score",
            "mse", "r2_score", "ai_score", "feedback", "problem_type"
        ])

    # -------------------------------
    # Remove old entry
    # -------------------------------
    leaderboard = leaderboard[leaderboard["student"] != result["student"]]

    # -------------------------------
    # Add new row
    # -------------------------------
    new_row = pd.DataFrame([{
        "student": result["student"],
        "score": result["final_score"],
        "accuracy": result["metrics"].get("accuracy"),
        "f1_score": result["metrics"].get("f1_score"),
        "mse": result["metrics"].get("mse"),
        "r2_score": result["metrics"].get("r2_score"),
        "ai_score": result["ai_score"],
        "feedback": result["feedback"],
        "problem_type": result["problem_type"]
    }])

    if leaderboard.empty:
        leaderboard = new_row
    else:
        leaderboard = pd.concat([leaderboard, new_row], ignore_index=True)

    # -------------------------------
    # Sorting logic
    # -------------------------------
    if result["problem_type"] == "classification":
        leaderboard = leaderboard.sort_values(
            by=["score", "accuracy", "f1_score", "ai_score"],
            ascending=[False, False, False, False]
        )
    else:
        leaderboard = leaderboard.sort_values(
            by=["score", "mse", "r2_score", "ai_score"],
            ascending=[False, True, False, False]
        )

    # -------------------------------
    # Save leaderboard
    # -------------------------------
    leaderboard.to_csv(path, index=False)

    print(f"🏆 Leaderboard updated for {result['student']}")


# ==========================================================
# 🔄 Run Evaluation for All Students
# ==========================================================
def run_all_evaluations(outputs_folder="outputs"):

    if not os.path.exists(outputs_folder):
        print("❌ Outputs folder not found")
        return

    files = [f for f in os.listdir(outputs_folder) if f.endswith("_predictions.csv")]

    if not files:
        print("⚠️ No prediction files found")
        return

    for file in files:
        student_name = file.replace("_predictions.csv", "")
        file_path = os.path.join(outputs_folder, file)

        result = run_evaluation(student_name, file_path)
        update_leaderboard(result)

    print("\n🎉 All evaluations completed!")


# ==========================================================
# 🚀 ENTRY POINT
# ==========================================================
if __name__ == "__main__":
    run_all_evaluations()