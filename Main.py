from helper import register, login, get_all_data, update_balance, Account, ACCOUNT_DB

def main():
  print("---------------------")
  print("Welcome.")
  print("1. Register")
  print("2. Log in")
  print("---------------------")
  print("")
  option = int(input())

  if option == 1:
    signup()
  elif option == 2:
    log_in()

def log_in():
  username = input("Enter your username: ")
  password = input("Enter your password: ")

  account = login(username, password)

  if account is None:
    print("")
    print("Invalid Username or Password")
    print("")
    log_in()
    return
  
  print("")
  print("Hi, " + account.firstname + "!")
  print("")

  show_account_options(account)


def signup():
  firstname = input("Enter your first name: ")
  lastname = input("Enter your last name: ")
  account_type = input("Enter your account type: ").lower()
  address = input("Enter your address: ")
  year = input("Enter the year: ")
  password = input("Enter your password: ")
  username = input("Enter a username: ")
  password = input("Enter a password: ")

  account = Account(firstname, lastname, account_type, address, year, username, password)
  register(account)

def check_balance(account):
  balance=account.balance
  print("")
  print("Your balance is: ")
  print("£{:,.2f}".format(balance))
  print("")
  show_account_options(account)

def deposit(account):
  print("")
  print("Enter Amount to be Deposited: ")
  amount=float(input("£"))
  print("")
  
  account.balance += amount
  update_balance(account, amount) 

  print("")
  print("Deposit Successful")
  print("Your New Balance is: ")
  print("£{:,.2f}".format(account.balance))
  print("")
  show_account_options(account)

def withdraw(account):
  print("")
  print("Enter Amount to be Withdrawn: ")
  amount=float(input("£"))
  print("")

  account.balance-=amount
  update_balance(account,amount)

  print("")
  print("Withdrawal Successful")
  print("Your New Balance is: ")
  print("£{:,.2f}".format(account.balance))
  print("")
  show_account_options(account)

def show_account_options(account):
  print("")
  print("---------------------")
  print("Select an Option:")
  print("1. Deposit")
  print("2. Withdraw")
  print("3. Check Balance")
  print("4. Log Out")
  print("---------------------")
  print("")
  option = int(input())
    
  if option == 1:
    deposit(account)
  elif option == 2:
    withdraw(account)
  elif option == 3:
    check_balance(account)
  elif option == 4:
    log_out()
      
def log_out():
  main()
