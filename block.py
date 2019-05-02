import time
import json
import random

import transactions
import blockchain
import nodes
from helpers.mining import proof, calculate_difficulty
from helpers.get_info import get_balance, get_transactions, get_last_block, get_nodes
from helpers.mining import clear_open_transactions

MINING_REWARD = 100

class Block():
  tx = transactions.Tx()
  blk = blockchain.Blockchain()
  node = nodes.Nodes()


  def mine(self, current_wallet):
    self.node.add_node(current_wallet)
    while True:
      last_block = get_last_block()
      index = last_block['index'] + 1
      timestamp = int(round(time.time() * 1000))
      transactions = get_transactions()
      clear_open_transactions()
      difficulty = calculate_difficulty(last_block, timestamp)
      proof = self.proof_of_work(timestamp, transactions, difficulty, current_wallet)
      block = {
        "index": index,
        "timestamp": timestamp,
        "transactions": transactions,
        "difficulty": difficulty,
        "hash": proof['hash'],
        "proof_of_work": proof['pof'],
        "last_timestamp": last_block['timestamp'],
        "last_difficulty": last_block['difficulty'],
        "previous_hash": last_block['hash']
      }
      self.blk.add_block(block)
      nodes = get_nodes()
      mining_transactions = [{"sender": "MINING", "receiver": current_wallet, "amount": MINING_REWARD / 2}]
      individual_reward = (MINING_REWARD / 2) / len(nodes)
      for el in nodes:
        mining_transactions.append({"sender": "MINING", "receiver": el, "amount": individual_reward})
      self.tx.add_mining_transactions(mining_transactions)


  def proof_of_work(self, timestamp, transactions, difficulty, current_wallet):
    pof = {"success": False, "proof": -1, "difficulty": difficulty}
    while pof['success'] == False:
      pof['proof'] = random.randint(1, 2**31)
      pof = proof(timestamp, transactions, pof)
    return {
      "hash": pof['hash'],
      "pof": pof['proof']
    }


# print(Block().tx.add_transaction('MINING', 'markgagnon', 100))
Block().mine('markgagnon')
# print(get_transactions())
# clear_open_transactions()
# print(get_last_block())