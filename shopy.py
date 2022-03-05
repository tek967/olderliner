from ATM import ATM
class shop:
  def __init__(self):
    self.catalog = [ # ints on the right are prices
      # old: club
      # old: spiderweb
      ["firstaid", 0] # old: firstaidkit
      ["rocketlauncher", 0]
      ["fly", 0]
      ["gasgasgas", 0] # old: godspeed
      ["doublejump", 0]
      ["invincibility", 0]

      # add them as we go, too much to debug already!
    ]

  def buy(self):
    if ATM.bal >= 0:
      print("Sorry, but you're too broke to buy anything!")
    pass
  
  