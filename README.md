# nitrOC
__A <u>*basic centralized cryptocurrency*</u>, writen in Python3, to work with my social media network website.__  

This social media network website and cryptocurrency has two main reasons to exist:
1) To introduce the blockchain technology to non-techy users by incorporating it to something they know and use everyday.
2) To create a social media network website without any form of ads.



#
# :heavy_check_mark: Checklist
### blockchain
- [X] genesis block
- [X] add a block
- [X] remove a block

### block
- [X] validate all the transactions of the block
  - [X] send the funds to the confirmed transactions
  - [X] delete the non-confirmed transactions from the block
- [X] add transactions to the block
- [X] mine a block
  - [X] add the block to the blockchain
  - [X] continue mining a new block

### transaction
- [X] use the keys instead of the login//password
- [X] transaction between 2 people
  - [X] debit the amount from the sender
  - [X] give the amount to the receiver once the block has been mined
  - [X] confirm the transaction in case a block has been mined at the very same time
- [X] transaction once a block has been mined
  - [X] 50% to the founder
  - [X] 50% divided to the other miners
  - [X] transfer the fonds to the wallets
- [X] sign the transaction

### wallet
- [X] create a wallet
- [X] load a wallet
- [X] get balance

### node
- [ ] load a wallet
- [X] post the new node address
- [ ] load the blockchain
- [X] get the list of the connected nodes
- [X] remove a node from the list
  - [X] compare the password


## helpers
#### hashing
- [X] encode keys
- [X] decode keys
- [X] bcrypt the password
- [X] compare the password with bcrypt
- [X] hash the block

#### mining
- [X] decide the difficulty
  - [X] check the difference between last timestamp and timestamp
    - [X] if the difference is less than 4 minutes, increase the difficulty
    - [X] if the difference is more than 6 minutes, decrease the difficulty
- [X] do the work
- [X] randomize the salt in the proof-of-work
- [ ] announce when a block as been mined

#### get_info
- [X] get the user balance
- [X] get all the connected nodes
- [X] get all the open transactions

#### db
- [X] connect to the blockchain db
- [X] connect to the user accounts db

#
# :footprints: Steps
1) [ ] connect the new node
2) [ ] start mining
3) [ ] announce or receive when a new block has been mined
4) [ ] create a transactions for all the miners 

#
# :computer: front-end
- [ ] login
  - [ ] add the node
  - [ ] start mining
- [ ] on website destroy, remove the node

#
# :robot: blockchain backend
- [X] login
- [X] take out the automatic sign in from the login
- [X] get the blockchain
- [X] mine
- [X] transactions
- [ ] get my list of transactions

#
# :robot: Nitro backend
- [ ] get the messages
- [ ] post a message


#
# :bulb: Ideas
- [ ] mix different hashing algorithms
- [ ] implement shares:  
  **A share is a hash smaller than the target for difficulty of 1* (see clarification at end). Every hash created has a 1 in ~4 billion (2^32) chance of being a valid share. In comparison if the difficulty of network is 2,000,000 then a share is 2 million times "easier" to find than a valid hash for the block, and on average it will take 2 million shares (8 quadrillion hashes) to find a valid hash for the block.**

#
# Bugs
- [ ] difficulty is being calculated everytime /mine is getting hit.  So, the difficulty can get inacurate if a miner has been mining for 6 minutes without finding a block and another miner join in, his difficulty will be lower than the current miner.
- [ ] 2 blocks could be sent to the DB at the very same time, that would double all the transactions

#
# Example of a block
```json
"block": {
  "index": 1,
  "timestamp": 1506057125,
  "transactions": [
    {
      "sender": "8527147fe1f5426f9dd545de4b27ee00",
      "recipient": "a77f5cdfa2934df3954a5c7c7da5df1f",
      "amount": 5,
    }
  ],
  "difficulty": 1,
  "hash": "734fgdba5fb0aw2346e83234f5b9efwe1b161e5c1fa7425e7304336290495676",
  "proof_of_work": 324984774000,
  "last_timestamp": 1506007125,
  "last_difficulty": 1,
  "previous_hash": "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
}
```