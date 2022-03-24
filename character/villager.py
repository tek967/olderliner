import pygame, random
from game.collision import CollisionControl
from character.pillager import Pillager
from currencyIO.data_io import Tools
from game.game import MainGame


class Villager:
    def __init__(self, MainGame):
        Tools.createFileIfNotExist(".villadotjar")
        self.villijar = open(".villadotjar")
        self.villidotjaread=self.villidotjar.read()
        self.villidotjarblit=pygame.self.Win.blit()

        self.chance = random.randint(0,1000000)

        self.villager = None
        
    def spawnChance(self):
        if self.villager == True:
            pass
        else:
            self.villager == False

    def attack(self):
        if None == None:
            pass
        



  