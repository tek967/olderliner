from ATM import ATM
class shop:
  def __init__(self):
    self.catalog = [ # ints on the middle are prices
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
    catalogselection = input("What would you like to buy?")
    # using nested for loops we can capture both dimensions of the array into the print statement
    for i in self.catalog:
      for j in i:
        print("Item \"{}\": {} Dollars", i, j)
    if catalogselection == "1":
      pass
    elif catalogselection == "2":
      pass
    elif catalogselection == "3":
      pass
    elif catalogselection == "4":
      pass
    elif catalogselection == "5":
      pass
    elif catalogselection == "6":
      pass

  
  