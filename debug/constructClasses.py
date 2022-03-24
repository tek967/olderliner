import sys
from currencyIO.setting import windew
from game.collision import CollisionControl
from game.map_io import mapy
from game.game import MainGame
from character.pillager import Pillager
from character.villager import Villager
from character.character import CharacterControl
from currencyIO.data_io import DataIO, Tools
from currencyIO.shopy import Shop

class init:
    def constructWindew():
        a = windew()
        sys.exit(0)
    def constructCollision():
        a = CollisionControl()
        sys.exit(0)
    def constructMapy():
        a = mapy()
        sys.exit(0)
    def constructMainGame():
        a = MainGame()
        sys.exit(0)
    def constructPillager():
        a = Pillager()
        sys.exit(0)
    def constructVillager():
        a = Villager()
        sys.exit(0)
    def constructCharacter():
        a = CharacterControl()
        sys.exit(0)
    def constructDataIO():
        a = DataIO()
        sys.exit(0)
    def constructShop():
        a = Shop()
        sys.exit(0)

    def menu():
        while True: 
            Tools.clear()

            print("DONT MESS WITH DEBUG TOOLS UNLESS IF YOU WANT TO")
            print("1. windew (settings)")
            print("2. Collision control")
            print("3. Mapy (inside map_io) ")
            print("4. MainGame (the game)")
            print("5. Pillager")
            print("6. Villager")
            print("7. Character")
            print("8. DataIO")
            print("9. Shop")

            choice = input("construct? ")

            if choice == "1":
                init.constructWindew()
            elif choice == "2":
                init.constructCollision()
            elif choice == "3":
                init.constructMapy()
            elif choice == "4":
                init.constructMainGame()
            elif choice == "5":
                init.constructPillager()
            elif choice == "6":
                init.constructVillager()
            elif choice == "7":
                init.constructCharacter()
            elif choice == "8":
                init.constructDataIO()
            elif choice == "9":
                init.constructShop()
            else:
                pass
        