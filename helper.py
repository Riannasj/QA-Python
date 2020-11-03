import csv
import shutil
from classes import Account

ACCOUNT_DB='data/accounts.csv'
TEMP_FILE='temp.csv'
FIELDS = ['Serial Number', 'First Name', 'Last Name', 'Address', 'Year', 'Balance', 'Username', 'Password']

def login(login_user, login_password):

  with open(ACCOUNT_DB, mode="r", encoding="utf-8", errors="ignore") as accounts_db:
     reader = csv.DictReader(accounts_db, delimiter=',', fieldnames=FIELDS)
     for row in reader:
       username = row['Username']
       password = row['Password']
       
       if username == login_user and password == login_password:
         account = marshal_account(row)
         return account

# Takes an account and inserts it into account database.
def register(account):
  serial_number = serial_number_gen(account)
  
  with open(ACCOUNT_DB, mode='a') as accounts_db:
    writer = csv.writer(accounts_db, delimiter=',')
    writer.writerow([serial_number, account.firstname, account.lastname, account.address, account.year, account.balance, account.username, account.password])
  return serial_number

# Generates a serial number using submitted account information.
def serial_number_gen(account):
  first_initial = account.firstname[0]
  last_initial = account.lastname[0]
  if account.account_type.lower() == "savings":
    type_letter = "S"
  elif account.account_type.lower() == "current":
      type_letter = "C"
  else:
        print("Account type needs to be either Savings or Current.")
        return
  serial_number = type_letter + last_initial + first_initial + str(account.year)
  return serial_number

# Retrieves all the data from the account database.
def get_all_data():

  data = []
  with open(ACCOUNT_DB, mode="r", encoding="utf-8", errors="ignore") as accounts_db:
    reader = csv.DictReader(accounts_db, delimiter=',', fieldnames=FIELDS)
    
    index = 0
    for row in reader:
      index += 1
      
      account = marshal_account(row)
      data.append(account)
      return data

def update_balance(account, amount):
  with open(ACCOUNT_DB, mode='r') as accounts_db, open(TEMP_FILE, 'w') as tempFile:
    reader = csv.DictReader(accounts_db, delimiter=',', fieldnames=FIELDS)
    writer = csv.DictWriter(tempFile, delimiter=',', fieldnames=FIELDS)

    for row in reader:
      if row['Serial Number'] == account.serial_number:
        row = {
          'Serial Number': account.serial_number,
          'First Name': account.firstname,
          'Last Name': account.lastname,
          'Address': account.address,
          'Year': account.year,
          'Username': account.username,
          'Password': account.password,
          'Balance': account.balance + amount
        }

        writer.writerow(row)

  shutil.move(TEMP_FILE, ACCOUNT_DB)
  
# Marshals a row of data into an account object
def marshal_account(row):
  serial_number = row['Serial Number']
  firstname = row['First Name']
  lastname = row['Last Name']
  address = row['Address']
  year = int(row['Year'])
  balance = float(row['Balance'])
  username = row['Username']
  password = row['Password']

  if serial_number[0] == "C":
    account_type = "Current"
  elif serial_number[0] == "S":
    account_type = "Savings"

  account = Account(firstname, lastname, account_type, address, year, username, password)
  account.serial_number = serial_number
  account.balance = balance

  return account