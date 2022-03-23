from character.villager import Villager
import pygame, random
from game.collision import CollisionControl
from game.game import MainGame

class Pillager:
    def __init__(self, MainGame):

        self.attack=20
        self.pillidotjar = open(".pillidotjar")
        self.pillidotjarread = self.pillidotjar.open()
        self.pillidotjarclose = self.pillidotjar.close()
        self.pilli = pygame.self.Win.blit()
        self.chance = random.randint(0,100000000000000000)
        self.pillager = None
        self.chance = random.randint(0,100000000000000000)
        
    def ifVillager(self):
        if None == None:
            pass
    
    def spawnPillager(self):
        if self.chance == 100:
            self.pillager = True
        else:
            self.pillager = False

    def placeholderName(self):
        pass