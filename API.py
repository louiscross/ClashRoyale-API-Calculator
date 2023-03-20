# imports required
import requests
from Card import Card
from Account import Account

# main class
class Main:
    def __init__(self, player_tag,auth):
        self.player_tag = player_tag
        self.headers = {
            "Accept": "application/json",
            "authorization": "Bearer "+auth

        }

    # not used in this release
    def updated_cards(self, newcardlist):
        print("Card Name\tLevel\tMax Level\tCount")
        print("--------")
        for card in newcardlist:
            print(f"{card.name}\t\t{card.level}\t{card.max_level}\t\t{card.count}")

    # function to get basic details for account ( name , current level, current exp toard next level) will apply this to object
    def getAccount(self, player_data):
        account_name = player_data['name']
        account_gold = 0
        account_level = player_data['expLevel']
        account_exp = player_data['expPoints']
        account = Account(account_name, account_gold,account_level, account_exp)
        return account
    
    # function to get all of the cards in your account, formatting them to cover name, card level, amount of cards and the card max level. This will be applied to object class and listed in card_data
    def getCards(self,cards,card_data):
            
            for card in cards:
                card_name = card['name']
                card_level = 14 - (card['maxLevel'] - card['level'])
                card_max_level = card['maxLevel']
                card_count = card['count']
                card = Card(card_name, card_level,card_max_level,card_count)
                card_data.append(card)
            return card_data
    
    # function to read data from text file and display level and exp to next level
    # we dont use cumulative exp currently, but could be useful in updates
    def exp_table(self,expTable):
        with open('exp_table.txt', 'r') as f:
            lines = f.readlines()
            
            for line in lines:
                line = line.strip().split('\t')
                level = int(line[0])
                exp_to_next_level = line[1].replace(',', '')
                cumulative_exp = int(line[2].replace(',', ''))
                
                expTable.append((level, exp_to_next_level, cumulative_exp))
        return expTable

    # function to read data from text file and display level and gold required to upgrade to next level. We only need to use the uncommon column as values are all the same
    # apart from legendaries to level 10 however we will counter this later.
    def upgrade_table(self,upgradeTable):
        with open('upgrade_table.txt', 'r') as f:
            lines = f.readlines()
            
            for line in lines:
                line = line.strip().split('\t')
                level = int(line[0])
                gold_to_next_level = line[1].replace(',', '')
                
                upgradeTable.append((level, gold_to_next_level))
        return upgradeTable
    
    # function to read data from text file and display level and exp required to upgrade to next level. We only need to use the uncommon column as values are all the same
    # apart from legendaries to level 10 however we will counter this later.
    def upgrade_table_exp(self,upgradeTableExp):
        with open('upgrade_table_exp.txt', 'r') as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip().split('\t')
                level = int(line[0])
                exp_to_next_level = line[1].replace(',', '')
                
                upgradeTableExp.append((level, exp_to_next_level))
        return upgradeTableExp
    
    def card_required_table(self,cardRequiredTable):
        with open('card_required_table.txt', 'r') as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip().split('\t')
                level = int(line[0])
                card_to_next_level_common = line[1].replace(',', '')
                card_to_next_level_rare = line[2].replace(',', '')
                card_to_next_level_epic = line[3].replace(',', '')
                card_to_next_level_legendary = line[4].replace(',', '')
                card_to_next_level_champion = line[5].replace(',', '')
                
                cardRequiredTable.append((level, card_to_next_level_common,card_to_next_level_rare,card_to_next_level_epic,card_to_next_level_legendary,card_to_next_level_champion))
        return cardRequiredTable
    



    def run(self):
        # initialise variables
        option = 0
        upgradeTableExp = []
        card_data = []
        upgradeTable = []
        expTable = []
        cardRequiredTable = []
        updatedcards = []
        
        # this index is used to determine which column to use on the card required table.
        itemRarityIndex = 0
        response = requests.get(f"https://api.clashroyale.com/v1/players/%23{self.player_tag}", headers=self.headers)

        # if response is good, then program will continue
        if response.status_code == 200:
            player_data = response.json()

            # this is the majority of data needed for the task.
            account = self.getAccount(player_data)
            cards = player_data['cards']
            card = self.getCards(cards,card_data)
            newcardlist = []
            expTable = self.exp_table(expTable)
            upgradeTable = self.upgrade_table(upgradeTable)
            upgradeTableExp = self.upgrade_table_exp(upgradeTableExp)
            cardRequiredTable = self.card_required_table(cardRequiredTable)
            DesiredLevel = input("\nplease enter desired level, must be above your current level and below 51: ")
            try:
                DesiredLevel = int(DesiredLevel)
            except ValueError:
                print("You did not enter an integer, please try again")
                main.run()

            if DesiredLevel > 50:
                print("Value is above 50 ( the highest level), please try again")
                main.run()

            if DesiredLevel < account.explevel:
                print("value is lower than your current level, please try again:\n")
                main.run()
            
            # main logic
            card = sorted(card_data, key=lambda x: x.level, reverse=False)
            while account.explevel != DesiredLevel:
                if not card:
                    print("-------\n\nnot enough cards to reach desired level.\n\nThe maximum level / exp you can achieve is:\nLevel: " + str(account.explevel) + "\nExperience: " + str(account.exppoints) + " / " + str(expTable[account.explevel][1]) + "\nCosting: " + f'{int(account.gold * -1):,}' + " gold\n\n--------")
                    return
                print("------")
                print(card[0])
                #These if statements are determining the quality of the card.
                if card[0].maxLevel == 14:
                    print("Common")
                    itemRarityIndex = 1
                if card[0].maxLevel == 12:
                    print("Rare")
                    itemRarityIndex = 2
                if card[0].maxLevel == 9:
                    print("Epic")
                    itemRarityIndex = 3
                if card[0].maxLevel == 6:
                    print("Legendary")
                    itemRarityIndex = 4
                if card[0].maxLevel == 4:
                    print("Champion")
                    itemRarityIndex = 5
                
                if card[0].level == 14:
                    print( str(card[0].name) + " is removed as level is max\n" )
                    newcardlist.append(card[0])
                    card_data.remove(card[0])
                    # update the card list that is sorted by level
                    card = sorted(card_data, key=lambda x: x.level, reverse=False)
                    continue
                #print(cardRequiredTable[card[0].level-1][itemRarityIndex])
                # This is the amount of cards required to level up
                #cardRequiredTable[card[0].level-1][itemRarityIndex]

                # if number of cards for card is less than the required amount to level up. We then delete from the list
                if card[0].count < int(cardRequiredTable[card[0].level-1][itemRarityIndex]):
                    print( str(card[0].name) + " is removed as not enough cards to upgrade:\n" + str(card[0].count) + "/" + str(cardRequiredTable[card[0].level-1][itemRarityIndex]))
                    target = card_data.index(card[0])
                    newcardlist.append(card_data[target])
                    card_data.remove(card[0])
                    # update the card list that is sorted by level
                    card = sorted(card_data, key=lambda x: x.level, reverse=False)
                    continue
                
                # if we have enough cards to upgrade then we do. We then add and subtract the neccessary information so our while loop can be continuously updated
                else: 


                    if card[0].level == 9 and card[0].maxLevel == 6:
                        card[0].count = int(card[0].count) - int(cardRequiredTable[card[0].level-1][itemRarityIndex])
                        card[0].level = int(card[0].level) + 1
                        print("Gold to upgrade: " + str(int(upgradeTable[card[0].level-2][1])-3000))
                        print("Experience from upgrade: " + str(int(upgradeTableExp[card[0].level-2][1])-150))
                        account.gold = account.gold - int(upgradeTable[card[0].level-2][1])-3000
                        account.exppoints = account.exppoints + int(upgradeTableExp[card[0].level-2][1])-150
                        print("has been upgraded to : " + str(card[0]))
                        card_data = [c if c.name != card[0].name else card[0] for c in card_data]
                        # update the card list that is sorted by level
                        card = sorted(card_data, key=lambda x: x.level, reverse=False)
                        
                        ##print(expTable[account.explevel][1])
                        ##print(account.exppoints)
                        if account.exppoints >= int(expTable[account.explevel][1]):
                            account.exppoints = account.exppoints - int(expTable[account.explevel][1])
                            account.explevel = account.explevel + 1
                        continue

                    #print(upgradeTable[card[0].level-1][1] )
                    card[0].count = int(card[0].count) - int(cardRequiredTable[card[0].level-1][itemRarityIndex])
                    card[0].level = int(card[0].level) + 1
                    print("Gold to upgrade: " + upgradeTable[card[0].level-2][1])
                    print("Experience from upgrade: " + str(int(upgradeTableExp[card[0].level-2][1])))
                    account.gold = account.gold - int(upgradeTable[card[0].level-2][1])
                    account.exppoints = account.exppoints + int(upgradeTableExp[card[0].level-2][1])
                    print("has been upgraded to: " + str(card[0]))
                    card_data = [c if c.name != card[0].name else card[0] for c in card_data]
                    # update the card list that is sorted by level
                    card = sorted(card_data, key=lambda x: x.level, reverse=False)
                    
                    
                #print(expTable[account.explevel][1])
                #print(account.exppoints)
                if account.exppoints >= int(expTable[account.explevel-1][1]):
                    account.exppoints = account.exppoints - int(expTable[account.explevel-1][1])
                    account.explevel = account.explevel + 1

                    print("--------\n\nYou have reached the requested leve!.\n\nYour new level is:\nLevel: " + str(account.explevel) + "\nExperience: " + str(account.exppoints) + " / " + str(expTable[account.explevel-1][1]) + "\nCosting: " + f'{int(account.gold * -1):,}' + " gold\n\n--------")
                    
                    
                    #option = input("Do you want to:\n1: see cards which have been updated\n2: calculate again with different desired level\n3: Exit\n")
                    #if option == "1":
                    #        print("Card Name\t\tLevel\t\tCount")
                    #        print("--------")
                    #        for card in newcardlist:
                    #            print(f"{card.name}\t\t{card.level}\t\t{card.count}")
                    
                
                            
        else:
            print(f"Error {response.status_code}: {response.text}")


if __name__ == '__main__':
    player_tag = input("please enter clash royale player tag, without the # : ")
    auth = input("please enter auth key from clash royale API: ")
    main = Main(player_tag,auth)
    main.run()

