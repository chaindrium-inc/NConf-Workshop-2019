"""
this python script was created by Simon Schuler (sschuler@chaindrium.com)
for the Workshop "Supply-Blockchain management" at NConf 2019
"""

import json
import binascii
from web3 import Web3, HTTPProvider
from eth_account import Account

# the rpc_endpoint (infura.io)
rpc_endpoint = "https://ropsten.infura.io/v3/0ec10f8ac6874f6a9a65515e4189ca47"

# init the web3 library for communicating with the blockchain
w3 = Web3(HTTPProvider(rpc_endpoint))
assert w3.isConnected()

# open the wallet we generated
with open("wallet/private.key", "rb") as key_file:
    account = Account().privateKeyToAccount(key_file.read())

print(w3.eth.getBalance(account.address))
