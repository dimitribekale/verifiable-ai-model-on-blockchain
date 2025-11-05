import hashlib
from datetime import datetime

def calculate_file_hash(file_path):
    """
    Calculate SHA256 hash of a file.
    - Reads file in chunks (4096 bytes at a time) to handle large files efficiently.
    - Returns an hexadecimal hash string (64 char)
    """
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)

        return sha256_hash.hexdigest()

def create_model_transaction(model_path, dataset_path, metrics, hyperparameters):
    """
    Create a transaction record containing all model info.
    It will be stored in the blockchain to prove the
    specific model file achieved specific metrics.
    - Returns a dict of transaction data.
    """
    transaction = {
        "timestamp": datetime.now().isoformat(),
        "model_hash": calculate_file_hash(model_path),
        "dataset_hash": calculate_file_hash(dataset_path),
        "metrics": metrics,
        "hyperparameters": hyperparameters,
    }
    return transaction