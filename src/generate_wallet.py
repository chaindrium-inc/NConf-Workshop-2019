"""
this python script was created by Simon Schuler (sschuler@chaindrium.com) 
for the Workshop "Supply-Blockchain management" at NConf 2019
"""

from eth_account import Account

# choose a random String
random_string = "put something randome here"

# create a new Account
account = Account().create(extra_entropy=random_string)

# save the private key in a file
with open("private.key", "wb") as key_file:
    key_file.write(account.privateKey)

# print all information on the screen
print("Address:", account.address)

# let the user know it succeded
print("Your key can be found in the file \"private.key\"")
