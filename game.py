import pygame
from data_io import settingsData

class maingame:
    def __init__(self):
        db = settingsData()
        self.winblow = open(".linerwindowsetting")
        self.Win = pygame.display.set_mode((db.settingArray[0][1],db.settingArray[0][2]))
        self.healthbar = 100
        self.mobDamage = 10
        self.slipperdamage=5
        self.mobhealth=5
        self.littlebrother=annoying
        