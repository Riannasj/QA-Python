import unittest

import csv
from helper import register, login, serial_number_gen, get_all_data, update_balance
from classes import Account

class TestDBSchema(unittest.TestCase):
    
    def test_serial_number_gen(self):
        account = generate_dummy_account()
        serial_number = serial_number_gen(account)
        self.assertEqual(serial_number, 'SJR2020')
        
    def test_register(self):
        account = generate_dummy_account()
        serial_number = register(account)
        data = get_all_data()
        last_account = data[-1]
        
        self.assertEqual(serial_number, last_account.serial_number)
        self.assertEqual(account.firstname, last_account.firstname)
        self.assertEqual(account.lastname, last_account.lastname)
        self.assertEqual(account.address, last_account.address)
        self.assertEqual(account.year, last_account.year)
        self.assertEqual(100, last_account.balance)
        self.assertEqual(account.username, last_account.username)
        self.assertEqual(account.password, last_account.password)
 
  # Register an account
  # Log in with username and password
  # Check to make sure account is returned from login   
    def test_login(self):
        account = generate_dummy_account()
        serial_number = register(account)

        logged_in_account = login(account.username, account.password)
        self.assertEqual(account.firstname, logged_in_account.firstname)
        self.assertEqual(account.lastname, logged_in_account.lastname)
    
    def test_update_balance(self):
        account = generate_dummy_account()
        account.balance += 50.55
        update_balance(account, account.balance)

        self.assertEqual(account.balance, 150.55)
    
def generate_dummy_account():
        firstname = "Rianna"
        lastname = "Johnson"
        account_type = "savings".lower()
        address = "13 Riddlesworth Road"
        year = 2020
        username = "username"
        password = "password"
        
        account = Account(firstname, lastname, account_type, address, year, username, password)
        account.balance = 100
        return account

if __name__ == '__main__':
  unittest.main()