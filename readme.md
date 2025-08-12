
# ClashRoyale API Level up calculator

This is a calculator which allows you to calculate the gold required to reach a desired level relative to the available cards in your account.
This program is build on [Python 3.9](https://www.python.org/downloads/release/python-390/) and uses the [Clash Royale API](https://developer.clashroyale.com/#/).

## Description

This is a simple tool to help you calculate how far you are from your next level or next king tower level. The logic of this tool is relatively straight forward. 

You use clashroyale's API to gather data from your account. Namely your current level, experience toard next level as well as all of the cards you currently hold, the levels which they are and the amount of each card.

We then sort these cards from its level ascending and take turns upgrading them. If the card doesnt have enough to be upgraded it is discarded. If the card is max level it is discarded. Once a card is upgraded. The account and card details will be updated to reflect this change and the loop will continue until either the desired level is reached or you run out of cards to upgrade.

![1 - W233Dbx](https://user-images.githubusercontent.com/118275848/226440257-834dd2c5-6c2e-478b-b6c1-f3cd84bedb56.png)
![2 - 49nBYso](https://user-images.githubusercontent.com/118275848/226440295-7d5fce29-5f5c-45c8-b0dc-2a07a8a1c1ff.png)

This are are the outcomes from one pass of the loop:

![3 - FeQArqN](https://user-images.githubusercontent.com/118275848/226440308-0366fd9b-d579-4b61-bc71-eee60c389dc4.png)
![4 - zjZp8gX](https://user-images.githubusercontent.com/118275848/226440322-6a7a44c0-35ac-4421-bb9e-7833a098a7b1.png)
![5 - ybcMc7W](https://user-images.githubusercontent.com/118275848/226440334-6b1f381d-61a2-4f4d-956c-33bc6c6b9833.png)

These next three images show the process of the card being upgraded until the point where the card cannot be upgraded further and is removed:

![6 - NKsplnk](https://user-images.githubusercontent.com/118275848/226440357-41dc8da0-20e6-45a4-868d-54b289079abe.png)
![7 - hseBBBG](https://user-images.githubusercontent.com/118275848/226440422-08d88c8f-07b3-47ba-b3e8-109d98d8418d.png)
![8 - trqv97o](https://user-images.githubusercontent.com/118275848/226440435-e52a547d-877b-46b2-86f4-ae5439681622.png)

Why did i make this? I have been playing the game for abit of time with friends and always seemed to wonder how long it would take to reach certain milestones, i went to google for this exact tool but to my suprise, out of all of the services between the wiki and fan made sites there seems to be nothing out there to solve this problem. This suprised me so i decided to put something together to solve this as im sure i am not the only person wanting to find out how far away i am to leveling up.


## How to compile and run

Firstly you will need python 3.9 installed, as well as the requests library.

you can install the requests library by using the command:

    pip install requests
in the command prompt.

apart from this, there are three pieces of data you need to find in order for the program to run. 

The first is a valid token from your [Clash Royale developer account](https://developer.clashroyale.com/#/). 
If you do not have an account create one for free, and once created follow through to [your account](https://developer.clashroyale.com/#/account) and create a key. The token generated will be needed for your program to run. and will be prompted for when the API.py is ran.

   
You just need to run clashroyaleUI.py to see the maximum available level


   
