from bson import ObjectId
import time

from helpers.db import connect_to_db_blockchain

class Blockchain:
  def __init__(self):
    db = connect_to_db_blockchain()
    self.blockchain = db.find_one({"_id": ObjectId("5cc8ec4efb6fc00ed59ea5fd")})
    print(blockchain)
    if len(self.blockchain['block']) == 0:
      self.genesis_block()


  def __repr__(self):
    return 'Number of blocks: ' + str(len(self.blockchain['block']))


  def genesis_block(self):
    block = {
      "index": 0,
      "timestamp": int(round(time.time() * 1000)),
      "transactions": [],
      "proof": "GENESIS",
      "hash": "GENESIS",
      "last timestamp": "GENESIS",
      "previous_hash": "GENESIS"
    }
    



blockchain = Blockchain()
print(blockchain)