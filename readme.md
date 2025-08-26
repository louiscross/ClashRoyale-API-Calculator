
# ClashRoyale API Level Up Calculator

This is a calculator which allows you to calculate the gold required to reach a desired level relative to the available cards in your account.
This program is build on [Python 3.9](https://www.python.org/downloads/release/python-390/) and uses the [Clash Royale API](https://developer.clashroyale.com/#/).

https://github.com/user-attachments/assets/2c9e87ea-1a88-456d-b4a6-6f4e3910c7d7



## How to compile and run

- Firstly you will need python 3.9 installed, as well as the requests library.

you can install the requests library by using the command:

    pip install requests

on the command line.

- Then run ClashRoyaleUI.py to login

<img width="1169" height="502" alt="image" src="https://github.com/user-attachments/assets/64c6085d-e4c0-4f81-8371-a3ecf934ca55" />


apart from this, there are two pieces of data you need to find in order to use the tool fully: 

- The first is a valid token from your [Clash Royale developer account](https://developer.clashroyale.com/#/).
  
If you do not have an account create one for free, and once created follow through to [your account](https://developer.clashroyale.com/#/account) and create a key.

- The second is your Clash Royale Player tag

Which you can find from your profile in game




## Description

This is a simple tool to help you calculate how far you are from your next level or next king tower level and the maximum capabilities of your account. The logic of this tool is relatively straight forward:

You use clashroyale's API to gather data from your account. Namely your current level, experience toard next level as well as all of the cards you currently hold, the levels which they are and the amount of each card.

We then sort these cards from its level ascending and take turns upgrading them. If the card doesnt have enough to be upgraded it is discarded. If the card is max level it is discarded. Once a card is upgraded. The account and card details will be updated to reflect this change and the loop will continue until either the desired level is reached or you run out of cards to upgrade.

Unfortunately the API only provides cards and card amounts as well as basic account info, it cannot show you gold on the account of magic items, so these we will have to enter manually.

The tool does not require you to make use of the magic items function, as forcing this would be annoying to those who want to save specific items. however if used it will aim to make the most efficient choices when consuming.

By default the tool aims to show you the maximum possible level of your account given its current state, however you can also use this to check the cost needed for individual levels

<img width="322" height="69" alt="image" src="https://github.com/user-attachments/assets/33f8314d-b589-402e-b7bd-8ca5592cea74" />

By using your real gold amount you will find out your maximum possible level given the amount of cards your account has, however you can choose to use an arbitrary high coin value to see what level you could reach given 

<img width="1143" height="466" alt="image" src="https://github.com/user-attachments/assets/d530e0bd-fb4b-44c9-87f7-b3d6b62d4b57" />
<img width="1146" height="503" alt="image" src="https://github.com/user-attachments/assets/c6bd15ec-783c-4499-9b68-c254e618ca07" />



## Motivation

Why did i make this? I have been playing the game for abit of time with friends and always seemed to wonder how long it would take to reach certain milestones, i went to google for this exact tool but to my suprise, out of all of the services between the wiki and fan made sites there seems to be nothing out there to solve this problem. This suprised me so i decided to put something together to solve this as im sure i am not the only person wanting to find out how far away i am to leveling up.


   



