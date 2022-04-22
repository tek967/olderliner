import sys, os
from currencyIO.ATM import ATM
from currencyIO.data_io import SettingsData as setting
from currencyIO.shopy import Shop as s

def main():
  while (True):
    try:
      choice = input("Welcome to liner! What to do?\n" + 
                    "1. Start the game in Pygame [incomplete]\n" + 
                    "3. Start the ATM [testing]\n" + 
                    "5. exit\n\n:"
                    )

      if choice == "1":
        os.system("clear")
        print("Told ya its not done yet!")
        pass
      if choice == "3":
        os.system("clear")
        ATM.ATMMenu(None)
        pass
      if choice == "5":
        os.system("clear")
        sys.exit(0)
      else:
        os.system("clear")
        print("Maybe try entering a valid choice?")

    except KeyboardInterrupt:
      print("\tDont be so abrupt with me! ")
      sys.exit(0)
      
if __name__ == "__main__":
  main()