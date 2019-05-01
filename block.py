import time
import json

import transactions
from helpers.mining import proof, calculate_difficulty
from helpers.get_info import get_balance

MINING_REWARD = 100

class Block:
  def mine(self, blockchain, current_wallet):
    index = blockchain[-1]['index'] + 1
    timestamp = int(round(time.time() * 1000))
    transactions = open_transactions
    difficulty = calculate_difficulty(blockchain, timestamp)
    proof = self.proof_of_work(timestamp, transactions, difficulty, current_wallet)
    return {
      "index": index,
      "timestamp": timestamp,
      "transactions": transactions,
      "difficulty": difficulty,
      "proof_of_work": proof,
      "last_timestamp": blockchain[-1]['last_timestamp'],
      "last_difficulty": blockchain[-1]['last_difficulty'],
      "previous_hash": blockchain[-1]['previous_hash']
    }

  def proof_of_work(self, timestamp, transactions, difficulty, current_wallet):
    pof = {"success": False, "proof": -1, "difficulty": difficulty}
    while pof['success'] == False:
      pof['proof'] += 1
      pof = proof(timestamp, transactions, pof)
    transactions.Tx.add_transaction('MINING', current_wallet, MINING_REWARD)
    return pof['proof']


blockchain = [{
  "index": 0,
  "last_timestamp": 1556651466600,
  "last_difficulty": 2,
  "previous_hash": "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
}]

open_transactions = [{
  "sender": 'Mark',
  "receiver": 'Marie',
  "amount": 5 
}, {
  "sender": 'Mark',
  "receiver": 'Elie',
  "amout": 2
}]

# print(Block().mine(blockchain, open_transactions, 'Mark'))
print(Block().mine(blockchain, 'markgagnon'))