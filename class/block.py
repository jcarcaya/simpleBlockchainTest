import time
import hashlib

class Block(object):

    def __init__(self,index,proof,previous_hash,transactions):
        self.index = index
        self.proof = proof
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.timestamp = time.time()

        @property
        def get_block_hash(self):
            block_string = "{}{}{}{}{}".format()
            return hashlib.sha256(block_string.encode()).hexdigest()