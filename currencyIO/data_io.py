import sys, os
from array import *

class Tools:
  def sort(array):
    for i in range(i, len(array)):
      key = array[i]
      j = i - 1
      while j >= 0 and key < array[j]:
        array[j+1] = array[j]
        key -= 1
      array[j+1] = key
    return array

  def clear():
    os.system("clear")

  def createFileIfNotExist(fileName):
    if os.path.exists(fileName) != True:
      open(fileName, "x")
    else:
      pass
  
  def print2DArray(array, shouldExit):
    for r in array:
      for c in r:
        print(c,end = " ")
      print()
    
    if shouldExit != False:
      sys.exit(0)

class SettingsData:
  def __init__(self) -> None:
    
    if os.path.exists(".linersettings") != True:
      Tools.createFileIfNotExist(".linersettings")
    
    self.settingsFile = open(".linersettings")

    self.settingsFormattedFile = self.settingsFile.readlines()

    self.settingArray = [
      ["winsize", None, None],
      ["playerName", None]
    ] 

    for i in range(len(self.settingArray)):
      for j in range(len(self.settingArray[i])):
        if self.settingArray[i][j] == "winsize" or self.settingArray[i][j] == "playerName":
          pass
        else:
          self.settingArray[i][j] = self.settingsFormattedFile[j] 
          # j will start from 0 too, just use this var for convenience

    Tools.print2DArray(self.settingArray, True)

  def writeTableToFile(self):
    for i in self.settingArray:
      self.writeSettings.write(self.settingArray[i])
      for j in i:
        self.writeSettings.write(self.settingArray[i][j])
  
  def writeSetting(key, ct1, ct2, self):
    for i in self.settingsArray:
      if i == key:
        self.settingArray[i][1] = ct1
        self.settingArray[i][2] = ct2
    SettingsData.writeTableToFile()


class DataIO: 
  def __init__(self):
    writeBf = None
    self.balance = open(".lineratm", "r")
    self.file = open(".lineratm", "w")
    self.pin = open(".linerpin", "r")
    self.pinWriter = open(".linerpin", "w")
    self.bankwriter = open(".linerbank","w")
    self.closeBal = self.file.close()
    self.closePIN = self.pin.close()
    self.error = None

  def deduct(deduct, self): 
    if int(self.balance) < deduct: 
      print("You're too broke to buy this.")
      return
    else:
      self.file = int(self.balance) - deduct
      return

  def withdraw(withdrawAmount, self):
    writeBf = self.bal + withdrawAmount
    self.bal.close()
    self.writeSettings.write(writeBf)
    return writeBf
    
  def deposit(depositAmount, self):
    writeBf = depositAmount - self.balance
    
    if (self.ball < depositAmount):
      print("Sorry, but you're too broke to withdraw that much.")
      
    self.file.write(writeBf)
    return writeBf
    
  def blank(self):
    self.bank.write(self.ball)
    
  def checkBal(self):
    return self.balance
    
  def getPin(self):
    return self.pin

  def writePin(newPin, self):
    self.pinWriter.write(newPin)
    return newPin

  def save_platform(self):
    pass