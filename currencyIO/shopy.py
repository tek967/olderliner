from ATM import ATM
from data_io import Tools
from array import *
from pynput.keyboard import Key, Listener

class Shop:
  def __init__(self):
    # item 0 = item id, item 1 = key, item 2 = price, item 3 = description, itme 4 = single use or not, item 5 = state
    self.list = [
      [ 0, "slippers", 8, "Use this to kill monsters.", True, None]
      [ 1, "block", 16, "a plain old block what do you expect?", True, None]
      [ 2, "spiderweb", 32, "Use this to pull u to a certain block.", False, None]
      [ 3, "firstaid", 64, "Revive your health", True, None ]
      [ 4, "godspeed", 128, "Use this to go too fast", False, None ]
      [ 5, "rocketlauncher", 256, "Use this to kill monsters or destory blocks", True, None]
      [ 6, "doubleJump", 512,"Jump twice, go high! ", False, None]
      [ 7, "fly", 1024,"you can fly... but u maybe will die from flying too high", True, None ]
      [ 8, "teleport", 2048,"teleport to certain block.", False, None ]
      [ 9, "invincible", 4096, "You can only die from your stupidity or cowardliness now! you can only invincible", True, None]
    ]
    
  def shopMenu(self):
    Tools.clear()
    print("Welcome to sohpyy!")
    print("please pick an item to purchase or view.")

    for i in self.list:
      print(self.list[i][0] + ".  " + self.list[i][1])

    print("press the number ID of the item you want to view/purchase.")
    
  def aboutPage(self):
    pass

  with Listener(on_press = shopMenu) as listener:
    listener.join()
  











