from bson import ObjectId

from helpers.hashing import password_compare
from helpers.db import connect_to_db_accounts, connect_to_db_blockchain

def get_balance(account_name):
  db = connect_to_db_accounts()
  account = db.find_one({"username": account_name})
  if account != '':
    return account['balance']
  else:
    return 'Wallet doesnt exist!'


def get_transactions():
  db = connect_to_db_blockchain()
  open_transactions = db.find_one({"_id": ObjectId("5cc8e412fb6fc00ed59ea3bb")})
  open_transactions = open_transactions['open_transactions']
  return open_transactions


def get_nodes():
  db = connect_to_db_blockchain()
  nodes = db.find_one({"_id": ObjectId("5cc9c967e7179a596b194ca1")})
  nodes = nodes['nodes']
  return nodes


def get_last_block():
  db = connect_to_db_blockchain()
  last_block = db.find_one({"_id": ObjectId("5cc8ec4efb6fc00ed59ea5fd")}, {"block":{'$slice': -1}})
  return last_block['block'][0]
