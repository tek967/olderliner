import pygame
class CharacterControl:
    def __init__(self,MainGame):
        self.character = open(".character")
        self.characteread = self.character.read()
        self.characterblit = pygame.self.Win.blit()