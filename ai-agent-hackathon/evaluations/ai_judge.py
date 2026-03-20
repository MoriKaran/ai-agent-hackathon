import json

# ==========================================================
# 🤖 AI JUDGE FUNCTION
# ==========================================================

def evaluate_with_ai(metrics, sample_predictions):
    """
    AI judge logic (rule-based for hackathon)
    MUST return JSON string
    """

    accuracy = metrics.get("accuracy", 0)
    f1 = metrics.get("f1_score", 0)
    problem_type = metrics.get("problem_type", "classification")

    # -------------------------------
    # Classification scoring
    # -------------------------------
    if problem_type == "classification":

        if accuracy > 0.9 and f1 > 0.85:
            score = 9
            feedback = "Excellent model 🚀 Strong performance."

        elif accuracy > 0.8:
            score = 7
            feedback = "Good model 👍 but can improve recall."

        elif accuracy > 0.7:
            score = 5
            feedback = "Decent model ⚠️ but missing patterns."

        else:
            score = 3
            feedback = "Weak model ❌ Improve features or tuning."

        if f1 < 0.5:
            feedback += " Model likely biased toward one class."

    # -------------------------------
    # Regression scoring
    # -------------------------------
    else:
        mse = metrics.get("mse", 1)
        r2 = metrics.get("r2_score", 0)

        if r2 > 0.9:
            score = 9
            feedback = "Excellent regression model 🚀"

        elif r2 > 0.75:
            score = 7
            feedback = "Good regression model 👍"

        elif r2 > 0.5:
            score = 5
            feedback = "Moderate performance ⚠️"

        else:
            score = 3
            feedback = "Poor regression model ❌"

    # -------------------------------
    # RETURN JSON STRING (IMPORTANT)
    # -------------------------------
    result = {
        "score": score,
        "feedback": feedback
    }

    return json.dumps(result)

#python evaluations/evaluate.py