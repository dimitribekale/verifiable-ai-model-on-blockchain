import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (accuracy_score,
                             f1_score,
                             precision_score,
                             recall_score)
from config import MODEL_CONFIG, MODELS_DIR, DEVICE

class ModelTrainer:

    def __init__(self):
        self.model = None
        self.metrics = None
        self.hyperparameters = None

    def train(self, X_train, y_train):
        self.model = RandomForestClassifier(
            n_estimators=MODEL_CONFIG["n_estimators"],
            random_state=MODEL_CONFIG["random_state"]
        )
        self.model.fit(X_train, y_train)

    def get_hyperparameters(self):
        hyperparameters = {
            "model_type": "random_forest",
            "n_estimators": MODEL_CONFIG["n_estimators"],
            "random_state": MODEL_CONFIG["random_state"],
            "test_size": MODEL_CONFIG["test_size"],
        }
        return hyperparameters
        
    def evaluate(self, X_test, y_test):
        """Evaluate the model and return a dict of metrics."""
        if self.model is None:
            raise ValueError("Model not trained. Call train() first.")
        predictions = self.model.predict(X_test)
        metrics = {
            "accuracy": float(accuracy_score(y_test, predictions)),
            "f1_score": float(f1_score(y_test, predictions, average="weighted")),
            "precision": float(precision_score(y_test, predictions, average="weighted")),
            "recall": float(recall_score(y_test, predictions, average="weighted")),
        }
        self.metrics = metrics
        return metrics
    
    def save_model(self, model_name):
        """Save the train model to the disk and returns the path."""
        if self.model is None:
            raise ValueError("No model to save.")
        MODEL_PATH = MODELS_DIR / f"{model_name}.pkl"
        with open(MODEL_PATH, "wb") as f:
            pickle.dump(self.model, f)
        return MODEL_PATH

