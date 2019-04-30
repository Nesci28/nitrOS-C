from helpers.hashing import password_compare, password_hash, encode, decode, create_keys
import pymongo
import os

# Load dotenv file
from dotenv import load_dotenv
from pathlib import Path
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


class Wallet():
  def load_wallet(self, account_name, account_password):
    db = wallet.connect_to_db()
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


  def get_balance(self, account_name, account_password):
    db = wallet.connect_to_db()
    account = db.find_one({"username": account_name})
    if password_compare(account_password, account['password']):
      return account['balance']
    else:
      return 'Wrong password!'


  def connect_to_db(self):
    DB_USERNAME = os.getenv("DB_USERNAME")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_URL = os.getenv("DB_URL")
    db = pymongo.MongoClient("mongodb://{}:{}@{}".format(DB_USERNAME, DB_PASSWORD, DB_URL))
    db = db['webserver']
    db = db["blockchain_accounts"]
    return db


wallet = Wallet()
wallet.load_wallet('test', 'test')
print(wallet.get_balance('test', 'test'))

print(30*'-')

wallet.load_wallet('markgagnon', 'root')
print(wallet.get_balance('markgagnon', 'root'))






