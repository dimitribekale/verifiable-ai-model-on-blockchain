from src.utils.hashing import calculate_file_hash

class Verifier:
    """Verifies if the model exists on the blockchain."""

    def __init__(self, blockchain):
        self.blockchain = blockchain

    def verify_model(self, model_path):
        """Returns a dict of verification results."""
        found = False
        model_hash = calculate_file_hash(model_path)
        for block in self.blockchain.chain:
            for transaction in block.transactions:
                if transaction.get("model_hash") == model_hash:
                    return {
                        "found": True,
                        "block_index": block.index,
                        "timestamp": transaction["timestamp"],
                        "metrics": transaction["metrics"],
                        "hyperparameters": transaction["hyperparameters"],
                    }

        return {
            "found": False,
            "message": "Model not found on the blockchain"
        }
    
    def verify_and_print(self, model_path):
        """Verify the model and print the results."""
        results = self.verify_model(model_path)
        if results["found"]:
            print("Model verified")
            print(f"    Block Index: {results['block_index']}")
            print(f"    Timestamp: {results['timestamp']}")
            print("     Metrics:")
            for metric_name, metric_value in results["metrics"].items():
                print(f"        - {metric_name}: {metric_value}")
        else:
            print(f"Model not found on blockchain")
            print(f"    {results.get('message', 'Unknown reason')}")
        
