import os
from pathlib import Path
from utils import get_device

BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
MODELS_DIR = BASE_DIR / "models"
BLOCKCHAIN_DIR = BASE_DIR / "blockchain_data"

MODEL_CONFIG = {
    "test_size": 0.2,
    "random_state": 42,
    "model_type": "random_forest",
    "n_estimators": 100,
}

BLOCKCHAIN_CONFIG = {
    "difficulty": 2,
    "mining_reward": 1,
}

HASHING_CONFIG = {
    "algorithm": "sha256",
    "chunk_size": 4096,
}

API_CONFIG = {
    "debug": True,
    "host": "0.0.0.0",
    "port": 5001,
    "max_content_length": 50 * 1024 * 1024,
}

LOGGING_CONFIG = {
    "level": "INFO",
    "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
}

FILE_NAMES = {
    "blockchain_data": "blockchain.json",
    "model_file": "model.pkl",
    "dataset_file": "dataset.csv",
}

METRICS_TO_TRACK = [
    "accuracy",
    "f1_score",
    "precision",
    "recall"
]

DEVICE = get_device()