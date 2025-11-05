from datetime import datetime
from src.blockchain.block import Block
from config import BLOCKCHAIN_CONFIG

class Blockchain:
    """
    Manages the entire blockchain:
    - Initialize with genesis block
    - Add transactions to pending list
    - Mine pending transactions into new blocks
    - Verify chain integrity
    """
    def __init__(self):
        """
        Initialize the blockchain with 
        empty chain and pending transactions
        """
        self.chain = []
        self.pending_transactions = []
        self.difficulty = BLOCKCHAIN_CONFIG["difficulty"]
        self.create_genesis_block()
    
    def create_genesis_block(self):
        """
        Create the first block in the chain (index 0).
        The genesis block contains no previous hash
        so previous_hash = "0"
        """
        if len(self.chain) == 0:
            block = Block(0, [], "0")
            self.chain.append(block)
        return self.chain[0]
    
    def get_latest_block(self):
        """Return the most recent block in the chain"""
        return self.chain[-1]
    
    def add_transaction(self, transaction):
        """Add a transaction to the pending list."""
        self.pending_transactions.append(transaction)
    
    def mine_pending_transactions(self, miner_address="system"):
        """Mine pending transactions into a new block"""
        if len(self.pending_transactions) == 0:
            print("No pending transactions to mine")
            return
        previous_block = self.get_latest_block()
        previous_hash = previous_block.hash
        
        new_block = Block(
            index=len(self.chain),
            transactions=self.pending_transactions.copy(),
            previous_hash=previous_hash
        )
        requirement = "0" * self.difficulty
        while not new_block.hash.startswith(requirement):
            new_block.nonce += 1
            new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)
        self.pending_transactions = []

    def is_chain_valid(self):
        """Verify the blockchain integrity"""
        chain = self.chain
        # Empty chain or only genesis block.
        if len(self.chain) <= 1:
            return True

        for i in range(1, len(chain)):
            current_block = chain[i]
            previous_block = chain[i-1]

            if current_block.hash != current_block.calculate_hash():
                return False
            
            if current_block.previous_hash != previous_block.hash:
                return False
            
            return True