import pygame

class character:
  def __init__(self):

    self.width = None
    self.height = None
    
    self.choose = input("\nhow large shall the game window be?\n" +  
                        "[d]efault: 600x800\n" + 
                        "[m]iddle 960x1024\n" + 
                        "[l]arge 1024x1400: ") 
    
    if (self.choose == "d"):
      self.height = 600
      self.width = 800
    elif (self.choose == "m"):
      self.height = 960
      self.width = 1024
    elif (self.choose == "l"):
      self.height = 1024
      self.width = 1400
    #endif

    self.name = input("hello travellers, whats your name?\n")
    self.Win = pygame.display.set_mode((self.width, self.height))
    
  def say(speech):
    print(speech)
  check_event=pygame.event
  if check_event==quit:
    pygame.QUIT()
