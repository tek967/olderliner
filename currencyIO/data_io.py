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

class SettingsData:

  def __init__(self) -> None:
    self.settingsFile = open(".linersettings")
    self.settingsFormattedFile = self.settingsFile.readlines()

    self.settingArray = [
      ["winsize",    None, None]
      ["playerName", None ]
    ]

    self.settingArray[0][1] = self.settingsFormattedFile[1]
    self.settingArray[0][2] = self.settingsFormattedFile[2]

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


class DataIo: 
  def __init__(self):
    writeBf = None
    self.balance = open(".lineratm", "r")
    self.file = open(".lineratm", "w")
    self.pin = open(".linerpin", "r")
    self.pinWriter = open(".linerpin", "w")
    self.bankwriter=open(".linerbank","w")

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
    pass