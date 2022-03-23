import pygame, random
from game.collision import CollisionControl
from character.pillager import Pillager
from game.game import MainGame


class Villager:
    def __init__(self, MainGame):
        self.villidotjar=open(".villidotjar")
        self.villidotjaread=self.villidotjar.read()
        self.villidotjarblit=pygame.self.Win.blit()

        self.chance = random.randint(0,100000000000000000)

        self.villager = None
        
    def spawnChance(self):
        if self.villager == True:
            pass
        else:
            self.villager == False

    def attack(self):
        if None == None:
            pass
        



  