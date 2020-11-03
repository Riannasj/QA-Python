class Account:
  def __init__(self, firstname, lastname, account_type, address, year, username, password):
    self.serial_number = ""
    self.firstname = firstname
    self.lastname = lastname
    self.account_type = account_type
    self.address = address
    self.year = year
    self.username = username
    self.password = password
    self.balance = 0