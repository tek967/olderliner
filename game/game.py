import pygame
from currencyIO.data_io import DataIo
from currencyIO.data_io import SettingsData

class MainGame:
    def __init__(self):
        db = SettingsData()
        self.Win = pygame.display.set_mode((db.settingArray[0][1],db.settingArray[0][2]))
        self.hp = 10
        