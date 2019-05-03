from helpers.hashing import password_compare, password_hash, encode, decode, create_keys, tx_signature, ver_signature
from helpers.get_info import get_balance, get_keys
from helpers.db import connect_to_db_accounts

class Wallet():
  def load_wallet(self, account_name, account_password):
    db = connect_to_db_accounts()
    account = db.find_one({"username": account_name})
    if account is not None:
      if password_compare(account_password, account['password']):
        if 'privateKey' not in account or 'publicKey' not in account:
          self.create_wallet(db, account_name, account_password) 
        else:
          public_key = decode(account_password, account['publicKey'])
          private_key = decode(account_password, account['privateKey'])
          balance = account['balance']
          message = {
            "message": {
              "public_key": public_key, 
              "private_key": private_key, 
              "balance": balance
            },
            "code": 200
          }
      else:
        message = {
          "message": "Wrong password!",
          "code": 401
        }
    else:
      message = {
        "message": "Account not found",
        "code": 201
      }
    return message

  
  def create_wallet(self, db, account_name, account_password):
    if db == '':
      db =connect_to_db_accounts()
    keys = create_keys(account_password)
    public_key = keys['public_key']
    private_key = keys['private_key']
    password = password_hash(account_password)
    db.insert_one({"username": account_name, "password": password, "privateKey": private_key, "publicKey": public_key, "balance": 10})
    message = {
      "message": "New account created: {}".format(account_name),
      "code": 200
    }
    return message


  @staticmethod
  def sign_transaction(public_key, private_key, receiver, amount):
    signature = tx_signature(public_key, private_key, receiver, amount)
    return signature


  @staticmethod
  def verify_transaction(transaction):
    verify_signature = ver_signature(transaction)
    return verify_signature


# wallet = Wallet()
# wallet.load_wallet('markgagnon', 'root')
# print(get_balance('markgagnon'))
