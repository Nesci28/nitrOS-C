from bson import ObjectId

from helpers.get_info import get_balance
from helpers.db import connect_to_db_blockchain, connect_to_db_accounts
from helpers.hashing import password_compare

class Tx:
  def add_transaction(self, sender, receiver, amount):
    if sender != "MINING":
      account_password = sender[1]
      sender = sender[0]
      db = connect_to_db_accounts()
      db_password = db.find_one({"username": sender})
      db_password = db_password['password']
      if password_compare(account_password, db_password):
        balance = get_balance(sender)
        liquidity = balance >= amount
        if liquidity:
          self.remove_liquidity(sender, balance, amount)
          transaction = {
            "sender": sender,
            "receiver": receiver,
            "amount": amount
          }
          print(transaction)
          self.insert_transaction(transaction)
          if self.confirm_transaction(db, transaction):
            print('Transaction confirmed')
          else:
            print('Transaction failed')
        else:
          print('Not enough credit')
      else:
          print('Wrong password')
    

  def confirm_transaction(self, db, transaction):
    db = connect_to_db_blockchain()
    find_tx = db.find_one(
      {
        "_id": ObjectId("5cc8e412fb6fc00ed59ea3bb"), 
        "open_transactions": transaction
      }
    )
    if find_tx != None:
      return True
    else:
      return False
  

  def add_mining_transactions(self, mining_transactions):
    self.insert_transaction(mining_transactions)

  
  def remove_liquidity(self, sender, balance, amount):
    db = connect_to_db_accounts()
    new_balance = balance - amount
    db.update_one({
      "username": sender
    }, { 
      '$set': { 
        "balance": new_balance
      }
    })


  def insert_transaction(self, transaction):
    db = connect_to_db_blockchain()
    db.find_one_and_update({
      "_id": ObjectId("5cc8e412fb6fc00ed59ea3bb")
      }, {
      '$push': {
        'open_transactions': transaction
      }
    })
    print('transaction added')
  
  
  
# tx = Tx()
# tx.add_transaction(['markgagnon', 'root'], 'Marie', 4)