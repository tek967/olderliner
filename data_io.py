import sys 
from ATM import bank as bkbal
class dataIo: 
  
  def __init__(self):
    writeBf = None
    self.balance = open(".lineratm", "r")
    self.file = open(".lineratm", "w")
    self.pin = open(".linerpin", "r")
    self.pinWriter = open(".linerpin", "w")
    self.bankwriter=open(".linerbank","w")
    self.bal=bkbal

  def withdraw(withdrawAmount, self):
    writeBf = self.balance + withdrawAmount
    self.file.write(writeBf)
    return writeBf
    
  def deposit(depositAmount, self):
    writeBf = depositAmount - self.balance
    
    if (self.balance < depositAmount):
      print("Sorry, but you're too broke to withdraw that much.")
      
    self.file.write(writeBf)
    return writeBf
    
  def balnk(self):
    self.bankwriter.write(self.bal)
    
  def checkBal(self):
    return self.balance
    
  def getPin(self):
    return self.pin

  def writePin(newPin, self):
    self.pinWriter.write(newPin)
    return newPin
    
  def save_platform(self):
    pass