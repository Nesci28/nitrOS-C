import hashlib

def proof(timestamp, transactions, pof):
  block = str(timestamp).encode('utf8') + str(transactions).encode('utf8') + str(pof['proof']).encode('utf8')
  hashed = hashlib.sha512(block).hexdigest()
  # print('hashed {}'.format(hashed))
  if hashed[0:pof['difficulty']] == pof['difficulty']*'0':
    return {"success": True, "proof": pof['proof'], "difficulty": pof['difficulty']}
  return {"success": False, "proof": pof['proof'], "difficulty": pof['difficulty']}


def calculate_difficulty(blockchain, timestamp):
  time_block = timestamp - blockchain[-1]['last_timestamp']
  if time_block < 5 * 60 * 1000:
    return blockchain[-1]['last_difficulty'] + 1
  return blockchain[-1]['last_difficulty']