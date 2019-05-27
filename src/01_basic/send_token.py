"""
this python script was created by Simon Schuler (sschuler@chaindrium.com)
for the Workshop "Supply-Blockchain management" at NConf 2019
"""

import json
import binascii
from web3 import Web3, HTTPProvider
from eth_account import Account

# set the new_owner (the person to send the token to)
new_owner = "0x0000000000000000000000000000000000000000"

# set the token Address
token_address = "0x6F5Ad512bdAC10DBE926D4963AE6523f9F6f1A88"

# the rpc_endpoint (infura.io)
rpc_endpoint = "https://ropsten.infura.io/v3/0ec10f8ac6874f6a9a65515e4189ca47"

# init the web3 library for communicating with the blockchain
w3 = Web3(HTTPProvider(rpc_endpoint))
assert w3.isConnected()

# load the contract-abi from the .abi file
with open("token_contract/NConfToken.abi") as abi_file:
    contract_abi = json.load(abi_file)

# load the token-contract with the address
token_contract = w3.eth.contract(abi=contract_abi, address=token_address)

# open the wallet we generated
with open("wallet/private.key", "rb") as key_file:
    account = Account().privateKeyToAccount(key_file.read())

# set transaction parameters
tx_param = {
    "from": account.address,
    "nonce": w3.eth.getTransactionCount(account.address),
    "gas": 1728712,
    "gasPrice": w3.toWei("21", "gwei")
}

# create transaction to send the token to another address
tx = token_contract.functions.give(new_owner).buildTransaction(tx_param)

# sign the transaction with the account
signed = account.signTransaction(tx)

# broadcast the transaction and get the hash back
tx_hash = w3.eth.sendRawTransaction(signed.rawTransaction)

# print the result
print("transaction hash: ", binascii.hexlify(tx_hash)[2:-1])
