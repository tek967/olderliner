import sys
from ATM import ATM

def main():
  choice = input("Welcome to liner! What to do?\n" + 
                 "1. Start the game in Pygame [incomplete]" + 
                 "2. Start the settings menu in CLI [incomplete]" +
                 "3. Start the ATM [testing]" + 
                 "4. Exit")
  if choice == "1":
    print("Told ya its not done yet!")
  if choice == "2":
    print("Told ya its not done yet!")
  if choice == "3":
    ATM.ATMMenu(None)
  if choice == "4":
    sys.exit(0)

if __name__ == "__main__":
  main()
