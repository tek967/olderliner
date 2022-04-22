import sys, multiprocessing
from multiprocessing import Queue as q #bruh so bri'ish
import threading
from console import console

from currencyIO import ATM,data_io,map_io,setting,shopy # othermodules


from game import collision,game
import main


class DebugTools:
    def __init__(self):
        self.cuio_debug = []
        self.game_debug = []
        self.main_debug = []
    def needle(self):
        pass
    def queue(self):
        pass

    def debugMain(menuProc):
        menuProc.start()
        console.log("started main menu,")

