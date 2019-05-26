"""
this python script was created by Simon Schuler (sschuler@chaindrium.com)
for the Workshop "Supply-Blockchain management" at NConf 2019
"""

import json
from web3 import Web3, HTTPProvider

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

# call the get_name function
token_name = token_contract.functions.get_name().call()

# print the result
print("token name:", token_name)
