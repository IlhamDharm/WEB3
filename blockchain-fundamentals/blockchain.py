
import hashlib
import json
from datetime import datetime

class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = str(datetime.now())
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_data = {
            "index": self.index,
            "timestamp": self.timestamp,
            "data": self.data,
            "previous_hash": self.previous_hash
        }

        encoded = json.dumps(
            block_data, sort_keys=True
        ).encode()

        return hashlib.sha256(encoded).hexdigest()


# Membuat genesis block
block1 = Block(0, "Genesis Block", "0")

# Membuat block kedua
block2 = Block(1, "Ilham mengirim 10 ETH", block1.hash)

print("Block 1:", block1.hash)
print("Block 2:", block2.hash)
print("Previous Hash:", block2.previous_hash)

print("Chain valid:",
      block2.previous_hash == block1.hash)
