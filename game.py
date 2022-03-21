import pygame
from data_io import settingsData

class maingame:
    def __init__(self):
        db = settingsData()
        self.winblow = open(".linerwindowsetting")
        self.Win = pygame.display.set_mode((db.settingArray[0][1],db.settingArray[0][2]))
        self.healthbar=10