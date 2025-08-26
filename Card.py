#This is your class for cards
class Card:
  def __init__(self, name, level,maxLevel,count):
    self.name = name
    self.level = level
    self.maxLevel = maxLevel
    self.count = count

  def __str__(self):
    # note maxLevel is not needed to be displayed. this is only needed for the upgrade of one level for one type of card.
    return f"{self.name} (Level: {self.level}, Count: {self.count})"

