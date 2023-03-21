# Name              : Git Account Switcher
# Description       : Switch account faster then typing the commands
# Author            : Elliott Fournier-Robert
# Creation Date     : March 21 2023

# 1 : Read file config to get all the accounts
# 2 : Put all the informations inside class Account and array of account
# 3 : Show the currently configured account
# 4 : Show menu and choice of user
# 5 : Set choosed account as configured account for git

# Imports
from os import system

# Account class
class Account:
    def __init__(self, name, username, email):
        self.name = name
        self.email = email
        self.username = username

# 1: Read config file
conf = open("config", "r")

# 2: Put all info inside class Account and array of accounts
accountArray = []
for line in conf :
    if line == "" :
        break
    else :
        line = line.split()
        account = Account(line[0], line[1], line[2])
        accountArray.append(account)

# 3: Show currently configured account
print("\nConfigured Username :")
system("git config user.name")
print("Configured Email :")
system("git config user.email")

# 4: Show menu and user choice
print("\n--Choose user--\n")
for i in accountArray:
    print(accountArray.index(i), " ", i.name)
userInput = input("\nChoice : ")

# 5: Configured choosen account
userInput = int(userInput)
system("git config --global user.name " + accountArray[userInput].username)
system("git config --global user.email " + accountArray[userInput].email)
print("Account was configured successfully !")