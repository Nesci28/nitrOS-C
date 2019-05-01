# nitroC

### blockchain
- [ ] genesis block
- [ ] add a block
- [ ] remove a block
- [ ] verify each block

### block
- [O] validate transation
- [X] add transactions
- [X] mine a block

### wallet
- [X] create a wallet
- [X] load a wallet
- [X] get balance

### node
- [ ] load a wallet
- [ ] load the blockchain
- [ ] get the list of the connected nodes
- [ ] post the new node address 


## helper
#### hashing
- [X] encode keys
- [X] decode keys
- [X] bcrypt the password
- [X] hash the block

#### proof-of-work
- [X] decide the difficulty
  - [X] check the difference between last timestamp and timestamp
- [X] do the work

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
  "previous_hash": "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
}
```