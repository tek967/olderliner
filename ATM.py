import sys
import os
from data_io import dataIo

class ATM:
  def __init__(self):
    self.inputBuffer = None
    self.loginState = False
    self.miscBuf = None
    self.bankbal = open(".linerbank","r")
    self.pinFile = ".linerpin"
    def clear():
      os.system("clear")
      
  def bank(self):
    pass

  def initAtm(self):
    self.clear()
    print("Welcome to the ATM!")
    
  def withdraw(self):
    if (self.inputBuffer != None):
      dataIo.withdraw(self.inputBuffer, None)
    elif (self.loginState == False):
      print("You need to log in First!")

    self.inputBuffer = input("How much money to withdraw?")
    dataIo.withdraw(self.inputBuffer, None)

  def deposit(self):
    if (self.inputBuffer != None):
      dataIo.withdraw(self.inputBuffer, None)
    elif (self.loginState == False):
      print("You need to log in First!")

    self.inputBuffer = input("How much money to deposit?")
    dataIo.deposit(self.inputBuffer, None)
    
  def createPin(create, self):
    if (create == True):
      if (os.exists(self.pinFile)):
        print("You already created the pin, just log in.")
        pass
      elif (create == False):
        os.remove(self.pinFile)

      pincode = None
      verifyPin = None

      for i in range(0, 3):
        pincode = input("What PIN to set?")
        verifyPin = input("Please enter the PIN again")
        
        if (pincode != verifyPin):
          if (i == 3):
            print("You tried too many times but the PIN code " + 
                "you reentered was incorrect, please try again later.")
          print("The PIN Codes do not match, Please try again.")
        else:
          misc = dataIo.writePin(verifyPin, None)
          if (misc != verifyPin):
            print("A FATAL ERROR OCCURED, PLEASE REPORT THIS ISSUE") 

  def login(self):

    verifyPin = None
    pin = None
    
    if (self.loginState == True):
      print("You don't need to log in, you are logged in already")
    for i in range(0, 3):
      pin = input("Enter your PIN: ")
      verifyPin = input("Enter your PIN again: ")
      if (pin != verifyPin):
        if (i == 3):
          print("You tried too many times but the PIN code " + 
                "you reentered was incorrect, please try again later.")
        print("The PIN Codes do not match, Please try again.")
      elif (dataIo.getPin(None) != verifyPin):
        print("You didn't enter the correct PIN.")
      else:
        self.loginState = true

  def ATMMenu(self):
    while (true):
      self.initAtm()
      choice = None
  
      print("Welcome to the ATM!\n" + 
            "What would you like to do?\n" + 
            "1. Log into the ATM \[{}\]\n" + 
            "2. Create an ATM Pin\n" + 
            "3. Change your ATM Pin\n" + 
            "4. Withdraw some money from your wallet\n" + 
            "5. Same money from your point store into your wallet"
            .format(this.loginState))
      choice = input("What to do?: ")
  
      if (choice == "1"):
        self.login(None)
      elif (choice == "2"):
        self.createPin(True, None)
      elif (choice == "3"):
        self.changePin(None)
      elif (choice == "4"):
        self.withdraw(None)
      elif (choice == "5"):
        self.deposit(None)


    
    
        
        
        
      