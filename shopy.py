class shop:
  def __init__(self):
    self.bel=open(".lineratm", "r")
    self.shoplist = ["club",
                     "spiderweb",
                     "firstaidkit",
                     "rocketlauncher",
                     "fly",
                     "godspeed",
                     "invisibility",
                     "doublejump",
                     "teleport",
                     "invincible"]
    self.price=open(".linerprice")

  def buy(self):
    if self.bal >= 0:
      pass
    pass
  
  