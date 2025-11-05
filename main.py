import sys
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

from config import DEVICE, DATA_DIR, MODEL_CONFIG
from src.blockchain.blockchain import Blockchain
from src.model.trainer import ModelTrainer
from src.utils.hashing import create_model_transaction
from src.verifier.verifier import Verifier

def main():
    print("="*60)
    print("Verifiable AI model on Blockchain - Demo")
    print("="*60)

    print("[INFO] - Loading the dataset -")
    iris = load_iris()
    X = iris.data
    y = iris.target

    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=MODEL_CONFIG["test_size"],
        random_state=MODEL_CONFIG["random_state"]
    )
    print("[INFO] - Dataset ready -")

    blockchain = Blockchain()
    trainer = ModelTrainer()
    trainer.train(X_train, y_train)
    print("[INFO] - Model trained -")
    print("[INFO] - Evaluation... -")
    metrics = trainer.evaluate(X_test, y_test)
    model_path = trainer.save_model("test_model")
    print("[INFO] - Model saved -")
    print("[INFO] - Creating a blockchain transaction -")
    data_path = DATA_DIR / "iris.csv"

    transaction_1 = create_model_transaction(model_path, data_path, metrics, trainer.get_hyperparameters())
    print("[INFO] - Mining block -")
    blockchain.add_transaction(transaction_1)
    blockchain.mine_pending_transactions()

    print("[INFO] - Verify model -")
    verifier = Verifier(blockchain)
    verifier.verify_and_print(model_path)

    print("[INFO] - Check blockchain integrity -")
    print(f"The blockchain is valid: {blockchain.is_chain_valid()}")

    print("="*60)
    print("Complete!!!")

if __name__ == "__main__":
    main()



