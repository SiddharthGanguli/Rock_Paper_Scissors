import os, json, logging
import joblib
from sklearn.metrics import f1_score

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

class ModelEvaluation:
    def __init__(self, model_path, test_data_path, metrics_dir="metrics", average="weighted"):
        self.model_path, self.test_data_path = model_path, test_data_path
        self.metrics_dir, self.average = metrics_dir, average

    def run(self):
        model = joblib.load(self.model_path)
        data = joblib.load(self.test_data_path)
        X, y = data["features"], data["labels"]

        y_pred = model.predict(X)
        f1 = f1_score(y, y_pred, average=self.average, zero_division=0) 

        os.makedirs(self.metrics_dir, exist_ok=True)
        out = os.path.join(self.metrics_dir, "f1.json")
        with open(out, "w") as f:
            json.dump({"f1_score": float(f1), "average": self.average}, f, indent=2)

        logging.info(f"F1 ({self.average}): {f1:.4f}")
        logging.info(f"Saved: {out}")
        return f1
