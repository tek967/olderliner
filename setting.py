from data_io import settingsData
class windew:
  def __init__(self):
    check_event=pygame.event

    self.width = None
    self.height = None
    
    if settingsData.settingArray[0][1] == None:
      if settingsData.settingArray[0][2] == None:
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

        settingsData.writeSetting(0, self.height, self.width, None)

      else:
        pass
    else:
      pass

    self.name = input("hello travellers, whats your name?\n")

  check_event = None
  if check_event == quit:
    pygame.QUIT()
