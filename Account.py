class Account:
    def __init__(self, name, gold, explevel, exppoints, elite_wild_cards=0, 
                 common_wild_cards=0, rare_wild_cards=0, epic_wild_cards=0, legendary_wild_cards=0, champion_wild_cards=0,
                 common_book=0, rare_book=0, epic_book=0, legendary_book=0, champion_book=0,
                 magic_coin=0):
        self.gold = gold
        self.name = name
        self.explevel = explevel
        self.exppoints = exppoints
        self.elite_wild_cards = elite_wild_cards
        
        # Wild Cards for each rarity
        self.common_wild_cards = common_wild_cards
        self.rare_wild_cards = rare_wild_cards
        self.epic_wild_cards = epic_wild_cards
        self.legendary_wild_cards = legendary_wild_cards
        self.champion_wild_cards = champion_wild_cards
        
        # Books for each rarity
        self.common_book = common_book
        self.rare_book = rare_book
        self.epic_book = epic_book
        self.legendary_book = legendary_book
        self.champion_book = champion_book
        
        # Magic Coin
        self.magic_coin = magic_coin

    
    def get_name(self):
        return self.name
    
    def get_explevel(self):
        return self.explevel
    
    def get_exppoints(self):
        return self.exppoints
    
    def get_gold(self):
        return self.gold
    
    def get_elite_wild_cards(self):
        return self.elite_wild_cards
    
    # Wild Card getters
    def get_common_wild_cards(self):
        return self.common_wild_cards
    
    def get_rare_wild_cards(self):
        return self.rare_wild_cards
    
    def get_epic_wild_cards(self):
        return self.epic_wild_cards
    
    def get_legendary_wild_cards(self):
        return self.legendary_wild_cards
    
    def get_champion_wild_cards(self):
        return self.champion_wild_cards
    
    # Book getters
    def get_common_book(self):
        return self.common_book
    
    def get_rare_book(self):
        return self.rare_book
    
    def get_epic_book(self):
        return self.epic_book
    
    def get_legendary_book(self):
        return self.legendary_book
    
    def get_champion_book(self):
        return self.champion_book
    
    # Magic Coin getter
    def get_magic_coin(self):
        return self.magic_coin