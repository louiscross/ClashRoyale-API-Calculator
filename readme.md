
# ClashRoyale API Level up calculator

This is a calculator which allows you to calculate the gold required to reach a desired level relative to the available cards in your account.
This program is build on [Python 3.9](https://www.python.org/downloads/release/python-390/) and uses the [Clash Royale API](https://developer.clashroyale.com/#/).

## Description

This is a simple tool to help you calculate how far you are from your next level or next king tower level. The logic of this tool is relatively straight forward. 

You use clashroyale's API to gather data from your account. Namely your current level, experience toard next level as well as all of the cards you currently hold, the levels which they are and the amount of each card.

We then sort these cards from its level ascending and take turns upgrading them. If the card doesnt have enough to be upgraded it is discarded. If the card is max level it is discarded. Once a card is upgraded. The account and card details will be updated to reflect this change and the loop will continue until either the desired level is reached or you run out of cards to upgrade.

![If you are able to reach your level required:](https://imgur.com/W233Dbx)

![if your card reaches max level](https://imgur.com/49nBYso)

![Removal of item from the card list due to lack of cards](https://imgur.com/FeQArqN)

![Catches the irregular experience / gold cost of legendaries at level 9](https://imgur.com/zjZp8gX)

![Removes card if cards arent available to meet upgrade cost](https://imgur.com/ybcMc7W)

These next three images show the process of the card being upgraded until the point where the card cannot be upgraded further and is removed:
![1/3](https://imgur.com/NKsplnk)
![2/3](https://imgur.com/hseBBBG)
![3/3](https://imgur.com/trqv97o)

Why did i make this? I have been playing the game for abit of time with friends and always seemed to wonder how long it would take to reach certain milestones, i went to google for this exact tool but to my suprise, out of all of the services between the wiki and fan made sites there seems to be nothing out there to solve this problem. This suprised me so i decided to put something together to solve this as im sure i am not the only person wanting to find out how far away i am to leveling up.


## How to compile and run

Firstly you will need python 3.9 installed, as well as the requests library.

you can install the requests library by using the command:

    pip install requests
in the command prompt.

apart from this, there are three pieces of data you need to find in order for the program to run. 

The first is a valid token from your [Clash Royale developer account](https://developer.clashroyale.com/#/). 
If you do not have an account create one for free, and once created follow through to [your account](https://developer.clashroyale.com/#/account) and create a key. The token generated will be needed for your program to run. and will be prompted for when the API.py is ran.

   
it is important you remove whitespaces before and after when inputting otherwise you will get a 403 response for invalid token.

Secondly you will need to find your player tag for clash royale. This can be found within the game on your profile as a # followed by 8 characters. you will need to use this when prompted by the program.

   it is also important to mention here that you should not include the hashtag in the variable. the request uses %23 in place of the hashtag abd has been added already. Failure to remove this will result in a 404 error.

Lastly you will be asked for the level you are wanting to obtain. When making it to this point all of the previous variables are correct and you are almost there. All you need to do is enter a valid level, if not it should be error handled and you will be reprompted. 


   
