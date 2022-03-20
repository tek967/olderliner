class shop:
  def __init__(self):
    # item 0 = item id, item 1 = key, item 2 = price, item 3 = description, itme 4 = single use or not
    self.list = [
      [ "slippers", 8, "Use this to kill monsters.", True ]
      [ "spiderweb", 16, "Use this to pull u to a certain block.", False ]
      [ "firstaid", 32, "Revive your health", True ]
      [ "godspeed", 64, "Use this to go too fast", False ]
      [ "rocketlauncher", 128, "Use this to kill monsters or destory blocks", True]
      [ "doubleJump", 256,"Jump twice, go high! ", False]
      [ "fly", 512,"you can fly... but u maybe will die from flying too high", True ]
      [ "teleport", 1024,"teleport to certain block.", False ]
      [ "invincible", 2048, "You can only die from your stupidity or cowardliness now! you can only invincible", True]
    ]

  def shopMenu(self):
    pass
  