from helpers.hashing import password_compare, password_hash, encode, decode, create_keys
from helpers.get_info import get_balance
from helpers.db import connect_to_db_accounts

class Wallet():
  def load_wallet(self, account_name, account_password):
    db = connect_to_db_accounts()
    account = db.find_one({"username": account_name})
    if account is not None:
      if password_compare(account_password, account['password']):
        if 'privateKey' not in account or 'publicKey' not in account:
          wallet.create_wallet(db, account_name, account_password) 
        else:
          public_key = decode(account_password, account['publicKey'])
          private_key = decode(account_password, account['privateKey'])
          balance = account['balance']
          return {"public_key": public_key, "private_key": private_key, "balance": balance}
      else:
        return "Wrong password!"
    else :
      wallet.create_wallet(db, account_name, account_password)

  
  def create_wallet(self, db, account_name, account_password):
    keys = create_keys(account_password)
    public_key = keys['public_key']
    private_key = keys['private_key']
    password = password_hash(account_password)
    db.insert_one({"username": account_name, "password": password, "privateKey": private_key, "publicKey": public_key, "balance": 10})





wallet = Wallet()
# wallet.load_wallet('markgagnon', 'root')
# print(get_balance('markgagnon'))
