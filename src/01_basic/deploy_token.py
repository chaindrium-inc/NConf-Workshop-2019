"""
this python script was created by Simon Schuler (sschuler@chaindrium.com)
for the Workshop "Supply-Blockchain management" at NConf 2019
"""

import json
import binascii
from web3 import Web3, HTTPProvider
from eth_account import Account

# the name of your token
token_name = "some name, please change"

# the rpc_endpoint (infura.io)
rpc_endpoint = "https://ropsten.infura.io/v3/0ec10f8ac6874f6a9a65515e4189ca47"

# init the web3 library for communicating with the blockchain
w3 = Web3(HTTPProvider(rpc_endpoint))
assert w3.isConnected()

# load the contract-abi from the .abi file
with open("token_contract/NConfToken.abi") as abi_file:
    contract_abi = json.load(abi_file)

# load the compiled binary of the contract from the .bin file
with open("token_contract/NConfToken.bin") as bin_file:
    contract_bin = "0x" + bin_file.read()

# init the token_contract object
token_contract = w3.eth.contract(abi=contract_abi, bytecode=contract_bin)

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

# call the constructor
# - give it the token_name as parameter
# build a transaction from that
# - give it the transaction parameters
tx = token_contract.constructor(token_name).buildTransaction(tx_param)

# sign the transaction with the account
signed = account.signTransaction(tx)

# broadcast the transaction and get the hash back
tx_hash = w3.eth.sendRawTransaction(signed.rawTransaction)

# print the result
print("transaction hash: ", binascii.hexlify(tx_hash)[2:-1])
