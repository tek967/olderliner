import sys 
from array import *

class settingsData:
  def __init__(self):
    self.settingsFile = open(".linersettings")
    self.writeSettings = open(".linersettings")
    self.settingsFormattedFile = self.settingsFile.readlines()

    settingArray = [
      ["winsize" , None, None]
    ]

    settingArray[0][1] = self.settingsFormattedFile[1]
    settingArray[0][2] = self.settingsFormattedFile[2]

  def writeTableToFile(self):
    for i in self.settingArray:
      self.writeSettings.write(self.settingArray[i])
      for j in i:
        self.writeSettings.write(self.settingArray[i][j])


  def writeSetting(entry, ct1, ct2, self):
    for i in self.settingsArray:
      if i == entry:
        self.settingArray[i][1] = ct1
        self.settingArray[i][2] = ct2
    settingsData.writeTableToFile()
          


class dataIo: 
  def __init__(self):
    self.bal = open(".lineratm")
    self.pin = open(".linerpin")
    self.bankwriter=open(".linerbank")
    self.ball=self.bal.read()
    self.bell=self.bal.write()
  def withdraw(withdrawAmount, self):
    writeBf = self.ball + withdrawAmount
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
    sys.platform()