from helpers.hashing import password_compare
from helpers.db import connect_to_db_accounts

def get_balance(account_name):
  db = connect_to_db_accounts()
  account = db.find_one({"username": account_name})
  if account != '':
    return account['balance']
  else:
    return 'Wallet doesnt exist!'