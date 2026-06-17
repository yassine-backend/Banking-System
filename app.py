import json
import os
import sys
import time
import random


accounts = {}

def cls():
     os.system('cls' if os.name == 'nt' else 'clear')

def save_db():
           with open("data.json", "w") as f:
             json.dump(accounts, f)

def laod_db(filename="data.json"):

    if not os.path.exists(filename):
        with open(filename, "w") as f:
            json.dump({}, f)
        return {}

    try:
        with open(filename, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        with open(filename, "w") as f:
            json.dump({}, f)
        return {}

accounts = laod_db()


def Create_Account():
    cls()
    try:
        print("=== Account System ===\n")
        name = str(input("Name:")).upper()
        if not name:
            cls()
            print("Please Insert Name!")
            time.sleep(0.8)
            return
        if name in accounts:
            print("Account Alrady In DB")
            time.sleep(0.8)
            return
        pin = random.randint(1000, 9999)
        balance = int(input("Balance:"))
        if balance < 0 :
            cls()
            print("Invalid Amount, User Cant Create Account With Negative He Need To TopUp")
            time.sleep(0.8)
            return
        accounts[name] = dict(account_value = pin, balance_value = balance)
        save_db()
        cls() 
        print("Account Created!")
        time.sleep(0.8)
        cls()
        print(f"*Name:{name}\n*Account Number:{accounts[name]["account_value"]}\n*Balance:{accounts[name]["balance_value"]}")
        input("Press Enter Back To Menu")
    except ValueError:
        cls()
        print("Invalid Input!")
        time.sleep(0.8)

def View_Accounts():
    cls()
    if not accounts:
        print("Empty!!!")
        time.sleep(0.8)
        return
    print("=== View Accounts ===\n")
    for i in accounts:
        print(f"*Name:{i}\n*Account Number:{accounts[i]["account_value"]}\n*Balance:{accounts[i]["balance_value"]}\n=========================")
    input("Press Enter Back To Menu")

def Search_Account():
    cls()
    print("===Search Account===")
    if not accounts:
        cls()
        print("Empty!")
        time.sleep(0.8)
    name = str(input("Name:")).upper()
    if not name:
        cls()
        print("Invalid Input!")
        time.sleep(0.8)
        return
    if name in accounts:
        cls()
        print("Founded!")
        time.sleep(0.5)
        cls()
        print(f"*Name:{name}\n*Account Number:{accounts[name]["account_value"]}\n*Balance:{accounts[name]["balance_value"]}\n===================")
        input("Press Enter Back To Menu")
    else:
        cls()
        print("Name Not Found In DB")
        time.sleep(0.8)

def Deposit_Account():
    cls()
    print("=== Deposit ===")
    if not accounts:
        cls()
        print("Empty!")
        time.sleep(0.8)
    name = str(input("Name:")).upper()
    if not name:
        cls()
        print("Invalid Input!")
        time.sleep(0.8)
        return
    if name in accounts:
        cls()
        print("Founded!")
        deposit = int(input("Amount:"))
        if deposit <0:
            cls()
            print("Invalid Amount")
            time.sleep(0.8)
        cls()
        accounts[name]["balance_value"] =  accounts[name]["balance_value"] + deposit
        save_db()
        print(f"*Name:{name}\n*Account Number:{accounts[name]["account_value"]}\n*Balance:{accounts[name]["balance_value"]}\n===================")
        input("Press Enter Back To Menu")
    else:
        cls()
        print("Name Not Found In DB")
        time.sleep(0.8)

def Withdraw_Account():
    cls()
    print("=== Withdraw ===")
    if not accounts:
        cls()
        print("Empty!")
        time.sleep(0.8)
    name = str(input("Name:")).upper()
    if not name:
        cls()
        print("Invalid Input!")
        time.sleep(0.8)
        return
    if name in accounts:
        cls()
        print("Founded!")
        Withdraw = int(input("Amount:"))
        if Withdraw <0:
            cls()
            print("Invalid Amount")
            time.sleep(0.8)
        cls()
        accounts[name]["balance_value"] =  accounts[name]["balance_value"] - Withdraw
        save_db()
        print(f"*Name:{name}\n*Account Number:{accounts[name]["account_value"]}\n*Balance:{accounts[name]["balance_value"]}\n===================")
        input("Press Enter Back To Menu")
    else:
        cls()
        print("Name Not Found In DB")
        time.sleep(0.8)

def Transfer_Money():
    cls()
    print("=== Transfer Money ===")
    if not accounts:
        cls()
        print("Empty!")
        time.sleep(0.8)
    name = str(input("Name of your account:")).upper()
    reciver = str(input("Name of account Recive Money:")).upper()
    if not name:
        cls()
        print("Invalid Input!")
        time.sleep(0.8)
        return
    if name in accounts and reciver in accounts:
        cls()
        print("Founded!!")
        time.sleep(0.8)
        cls()
        amount = int(input("Amount to send"))
        accounts[name]["balance_value"] = accounts[name]["balance_value"] - amount
        accounts[reciver]["balance_value"] = accounts[reciver]["balance_value"] + amount
        save_db()
        print("=== Sender ===\n")
        print(f"*Name:{name}\n*Account Number:{accounts[name]["account_value"]}\n*Balance:{accounts[name]["balance_value"]}\n===================")
        print("=== Reciver ====\n")
        print(f"*Name:{reciver}\n*Account Number:****\n*Balance: +{amount}\n===================")
        input("Press Enter Back To Menu")
    else:
        cls()
        print("check The Names!!!")
        time.sleep(0.8)

def Delete_Account():
    cls()
    print("=== Delete Account ===")
    if not accounts:
        cls()
        print("Empty!")
        time.sleep(0.8)
    name = str(input("Name:")).upper()
    if not name:
        cls()
        print("Invalid Input!")
        time.sleep(0.8)
        return
    if name in accounts:
        cls()
        print("Deleted!")
        time.sleep(0.8)
        cls()
        accounts.pop(name)
        save_db()
        input("Press Enter Back To Menu")
    else:
        cls()
        print("Name Not Found In DB")
        time.sleep(0.8)

def Statistics():
    cls()
    print("=== Statistics ===")
    Total_Players = 0
    richest = ""
    if not accounts:
        cls()
        print("Empty!")
        time.sleep(0.8)
        return
    max_value = max(v["balance_value"] for v in accounts.values())
    gen = (v["balance_value"] for v in accounts.values())
    for i in accounts:
        if max_value == accounts[i]["balance_value"]:
            richest = i
    Total_Money = sum(gen)


    for i in accounts:
        Total_Players += 1 

    print(f"Total Accounts: {Total_Players}") 
    print(f"Total Money In Bank:{Total_Money}")
    print(f"Richest Account: {richest} {max_value}") 
    input("Press Enter Back To Menu")


while True:
     cls()
     try:
        print("=== Banking System ===\n")
        print("1. Create Account\n2. View Accounts\n3. Search Account\n4. Deposit\n5. Withdraw\n6. Transfer Money\n7. Delete Account\n8. Statistics\n9. Logout")
        Choise = int(input())
        if Choise == 1:
            Create_Account()
        elif Choise == 2:
            View_Accounts()
        elif Choise == 3:
            Search_Account()
        elif Choise == 4:
            Deposit_Account()
        elif Choise == 5:
            Withdraw_Account()
        elif Choise == 6:
            Transfer_Money()
        elif Choise == 7:
            Delete_Account()
        elif Choise == 8:
            Statistics()
        else:
            cls()
            print("Wrong Value!")
            time.sleep(0.5)
     except ValueError:
         cls()
         print("Invalid Input!!")
         time.sleep(0.5)