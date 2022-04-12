import sys, os, time, threading
from currencyIO.data_io import DataIO, Tools

class ATM:
  def __init__(self) -> None:
    self.inputBuffer = None
    self.loginState = False

    Tools.createFileIfNotExist(".linerbal")
    Tools.createFileIfNotExist(".linerbankbal")
    
    self.bal = open(".linerbal")
    self.pinFile = open(".linerpin")
    self.bankbal = open(".linerbankbal")
      
  def bank(self):
    time.Time()
    time.sleep(3600)
    threading.thread()

  def initAtm(self):
    os.system("clear")
    print("Welcome to the ATM!")

  def withdraw(self):
    if (self.inputBuffer != None):
      DataIO().withdraw(inputBuffer)
    elif (self.loginState == False):
      print("You need to log in First!")

    inputBuffer = input("How much money to withdraw?")
    DataIO().withdraw(inputBuffer)

  def deposit(self):
    if (inputBuffer != None):
      DataIO().withdraw(inputBuffer)
    elif (self.loginState == False):
      print("You need to log in First!")

    inputBuffer = input("How much money to deposit?")
    DataIO().deposit(inputBuffer)
    
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
          misc = DataIO().writePin(verifyPin)
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
      elif (DataIO().getPin() != verifyPin):
        print("You didn't enter the correct PIN.")
      else:
        loginState = True

  def ATMMenu(self):
    while (True):
      p = ATM()
      p.initAtm() 
      choice = None
  
      print("Welcome to the ATM!\n" + 
            "What would you like to do?\n" + 
            "1. Log into the ATM [should show the login state]\n" + 
            "2. Create an ATM Pin\n" + 
            "3. Change your ATM Pin\n" + 
            "4. Withdraw some money from your wallet\n" + 
            "5. Save money from your point store into your wallet\n"
            "6. exit\n"
            "7. *testing* bank\n"
           )
      
      choice = input("What to do?: ")
  
      if choice == "1":
        p.login()
      elif choice == "2":
        p.createPin(True)
      elif choice == "3":
        p.changePin(ATM)
      elif choice == "4":
        p.withdraw(ATM)
      elif choice == "5":
        p.deposit(ATM)
      elif choice=="6":
        sys.exit(0)
      elif choice=="7":
        p.bank(ATM)