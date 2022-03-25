import pygame, os
from currencyIO.data_io import Tools

class mapy:
    def __init__(self):
        Tools.createFileIfNotExist(".linermap")
        self.maps = open(".linermap")

    def generatemap(self):
        self.maps = None
        pass