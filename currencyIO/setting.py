from ATM import ATM
from data_io import SettingsData
import pygame
class windew:
  def __init__(self):
    self.check_event = pygame.event

    self.width = None
    self.height = None
    
    if SettingsData.settingArray[0][1] == None:
      if SettingsData.settingArray[0][2] == None:
        self.choose = input("\nhow large shall the game window be?\n" +  
                            "[d]efault: 600x800\n" + 
                            "[m]iddle 960x1024\n" + 
                            "[l]arge 1024x1400: ") 
        
        if self.choose == "d":
          self.height = 600
          self.width = 800
        elif self.choose == "m":
          self.height = 960
          self.width = 1024
        elif self.choose == "l":
          self.height = 1024
          self.width = 1400

        SettingsData.writeSetting(0, self.height, self.width, None)

      else:
        pass
    else:
      pass

  ATM.check_event = None
  if ATM.check_event == quit:
    pygame.QUIT()
