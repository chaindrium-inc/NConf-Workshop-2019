"""
this python script was created by Simon Schuler (sschuler@chaindrium.com) 
for the Workshop "Supply-Blockchain management" at NConf 2019
"""

from eth_account import Account

# choose a random String, acts as a seed for wallet generation
# this just increases the entropy, executing this script twice with the same
# random_string dose not produce the same wallet!
random_string = "put something randome here"

# create a new Account
account = Account().create(extra_entropy=random_string)

# save the private key in a file
with open("wallet/private.key", "wb") as key_file:
    key_file.write(account.privateKey)

# print all information on the screen
print("Address:", account.address)

# let the user know it succeded
print("Your key can be found in the file \"wallet/private.key\"")
