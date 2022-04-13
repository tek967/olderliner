import sys
from multiprocessing import Queue as q #bruh so bri'ish
import threading

from currencyIO import ATM,data_io,map_io,setting,shopy # othermodules


from game import collision,game
import main


class DebugTools: #eathorn so debug takes one thread,game takes one thread,map_io takes one thread,collision takes one thread. wow threads, concurrency
    def __init__(self):
        self.cuio_debug = []
        self.game_debug = []
        self.main_debug = []
    def needle(self):
        pass
    def queue(self):
        pass
    def switch(self):
        self.debu = threading.start_new_thread(DebugTools.needle())
        self.thread_set_name = threading.setName("debug")
        self.thread_start = threading.start()
        self.thread_listening = threading.current_Thread()
        self.thread_alive_listener = threading.isAlive()
        self.thread_watching = threading.run()
        


        
