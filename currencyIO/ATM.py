import sys, os, time
from data_io import DataIO
import threading

class ATM:
  def __init__(self) -> None:
    self.inputBuffer = None
    self.loginState = False
    self.bal = open(".linerbal","r")
    self.pinFile = (".linerpin","r")
    self.bankbal = open(".linerbankbal","r")
    
      
  def bank(self):
    time.Time()
    time.sleep(3600)
    threading.thread()

  def initAtm(self):
    os.system("clear")
    print("Welcome to the ATM!")

  def withdraw(self):
    if (self.inputBuffer != None):
      DataIO.withdraw(inputBuffer, DataIO.__init__)
    elif (self.loginState == False):
      print("You need to log in First!")

    inputBuffer = input("How much money to withdraw?")
    DataIO.withdraw(inputBuffer, DataIO.__init__)

  def deposit(self):
    if (inputBuffer != None):
      DataIO.withdraw(inputBuffer, DataIO.__init__)
    elif (self.loginState == False):
      print("You need to log in First!")

    inputBuffer = input("How much money to deposit?")
    DataIO.deposit(inputBuffer, DataIO.__init__)
    
  def createPin(create, self):
    pinfile = '.linerpin'
    if (create == True):
      if (os.path.exists(".linerpin")):
        print("You already created the pin, just log in.")
        pass
      elif (create == False):
        os.remove(pinfile)

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
          misc = DataIO.writePin(verifyPin, None)
          if (misc != verifyPin):
            print("A FATAL ERROR OCCURED, PLEASE REPORT THIS ISSUE") 

  def login(self):

    verifyPin = None
    pin = None
    
    if (loginState == True):
      print("You don't need to log in, you are logged in already")
    for i in range(0, 3):
      pin = input("Enter your PIN: ")
      verifyPin = input("Enter your PIN again: ")
      if (pin != verifyPin):
        if (i == 3):
          print("You tried too many times but the PIN code " + 
                "you reentered was incorrect, please try again later.")
        print("The PIN Codes do not match, Please try again.")
      elif (DataIO.getPin(None) != verifyPin):
        print("You didn't enter the correct PIN.")
      else:
        loginState = True

  def ATMMenu(self):
    while (True):
      p = ATM
      p.initAtm(ATM.__init__) 
      choice = None
  
      print("Welcome to the ATM!\n" + 
            "What would you like to do?\n" + 
            "1. Log into the ATM [should show the login state]\n" + 
            "2. Create an ATM Pin\n" + 
            "3. Change your ATM Pin\n" + 
            "4. Withdraw some money from your wallet\n" + 
            "5. Same money from your point store into your wallet\n"
            "6. exit\n"
            "7. *testing* bank\n"
           )
      
      choice = input("What to do?: ")
  
      if choice == "1":
        p.login(ATM.__init__)
      elif choice == "2":
        p.createPin(True, ATM.__init__)
      elif choice == "3":
        p.changePin(ATM.__init__)
      elif choice == "4":
        p.withdraw(ATM.__init__)
      elif choice == "5":
        p.deposit(ATM.__init__)
      elif choice=="6":
        sys.exit(0)
      elif choice=="7":
        p.bank(ATM.__init__)

