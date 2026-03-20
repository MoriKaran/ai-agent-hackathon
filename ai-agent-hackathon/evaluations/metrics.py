from sklearn.metrics import (
    accuracy_score,
    f1_score,
    mean_squared_error,
    r2_score
)

def calculate_metrics(y_true, y_pred):

    results = {}

    # Detect classification (0/1 or small integers)
    unique_values = set(y_true)

    if len(unique_values) <= 10:
        try:
            results["accuracy"] = accuracy_score(y_true, y_pred)
            results["f1_score"] = f1_score(y_true, y_pred, average="weighted")
            results["problem_type"] = "classification"
        except:
            pass

    # Regression fallback
    else:
        try:
            results["mse"] = mean_squared_error(y_true, y_pred)
            results["r2_score"] = r2_score(y_true, y_pred)
            results["problem_type"] = "regression"
        except:
            pass

    return results