class Account:
    def __init__(self, name,gold, explevel, exppoints):
        self.gold = gold
        self.name = name
        self.explevel = explevel
        self.exppoints = exppoints

    
    def get_name(self):
        return self.name
    
    def get_explevel(self):
        return self.explevel
    
    def get_exppoints(self):
        return self.exppoints
    
    def get_gold(self):
        return self.gold