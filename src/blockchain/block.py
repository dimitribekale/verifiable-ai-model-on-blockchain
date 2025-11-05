import json
import hashlib
from datetime import datetime

class Block:
    """
    Single block in the blockchain.
    Each block contains:
    - index: Position in the chain (0, 1, 2, ...)
    - timestamp: When the block was created
    - transactions: List of records (model performance data)
    - previous_hash: Hash of the previous block (links in the chain)
    - nonce: A number we increment to find valid hash (proof-of-work)
    - hash: This block's unique fingerprint.
    """
    def __init__(self, index, transactions, previous_hash):
        self.index = index
        self.timestamp = datetime.now().isoformat()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """Create SHA256 hash of this block's data"""
        block_data = {
            "index": self.index,
            "timestamp": self.timestamp,
            "transactions": self.transactions,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce,
        }
        block_string = json.dumps(block_data, sort_keys=True)
        block_hash = hashlib.sha256(block_string.encode()).hexdigest()
        return block_hash
