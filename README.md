# nitroC

### blockchain
- [ ] genesis block
- [ ] add a block
- [ ] remove a block
- [ ] verify each block

### block
- [ ] validate transation
- [X] add transactions
- [X] mine a block

### transaction
- [X] transaction between 2 people
  - [X] debit the amount from the sender
- [ ] transaction for the block founder
  - [ ] 50% to the founder
  - [ ] 50% divided pro-rata to the other miners

### wallet
- [X] create a wallet
- [X] load a wallet
- [X] get balance

### node
- [ ] load a wallet
- [ ] load the blockchain
- [ ] get the list of the connected nodes
- [ ] post the new node address 


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

#### get_info
- [X] get the user balance

#### db
- [X] connect to the blockchain db
- [X] connect to the user accounts db

```json
"block": {
  "index": 1,
  "last timestamp": 1506007125,
  "timestamp": 1506057125,
  "transactions": [
    {
      "sender": "8527147fe1f5426f9dd545de4b27ee00",
      "recipient": "a77f5cdfa2934df3954a5c7c7da5df1f",
      "amount": 5,
    }
  ],
  "proof": 324984774000,
  "hash": "734fgdba5fb0aw2346e83234f5b9efwe1b161e5c1fa7425e7304336290495676",
  "previous_hash": "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
}
```