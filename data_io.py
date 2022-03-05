from ntpath import join
import sys 
from array import *
from ATM import bank as bkbal

class settingsData:
  def __init__(self):
    settingsFile = open(".linersettings")
    settingsFormattedFile = settingsFile.readlines()

    settingArray = [
      ["winsize" , None, None]
    ]

    settingArray[0][1] = settingsFormattedFile[1]
    settingArray[0][2] = settingsFormattedFile[2]

  def writeTableToFile(self):
    for i in self.settingArray:
      self.settingsFile.write(self.settingArray[i])
      for j in i:
        self.settingsFile.write(self.settingArray[i][j])


  def writeSetting(entry, ct1, ct2, self):
    for i in self.settingsArray:
      if i == entry:
        self.settingArray[i][1] = ct1
        self.settingArray[i][2] = ct2
    settingsData.writeTableToFile()
          


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