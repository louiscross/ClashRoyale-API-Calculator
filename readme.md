# ClashRoyale Level up calculator

This is a calculator which allows you to calculate the gold required to reach a desired level relative to the available cards in your account.

This program is build on [Python 3.9](https://www.python.org/downloads/release/python-390/) and uses the [Clash Royale API](https://developer.clashroyale.com/#/).


## How to compile and run

Firstly you will need python 3.9 installed, as well as the requests library.

you can install the requests library by using the command:

    pip install requests
in the command prompt.

apart from this, there is two pieces of data you need to find in order for the program to run. 

The first is a valid token from your [Clash Royale developer account](https://developer.clashroyale.com/#/). 
If you do not have an account create one for free, and once created follow through to [your account](https://developer.clashroyale.com/#/account) and create a key. The token generated will be needed for your program to run. and will be added in the code after Bearer.

    headers = {
	    "Accept": "application/json",
	    "authorization": "Bearer YOUR_TOKEN"
	    }
it is important you only replace YOUR_TOKEN and keep Bearer othwise you will get a 403 response for invalid token.

Secondly you will need to find your player tag for clash royale. This can be found within the game on your profile as a # followed by 8 characters. you will need to use this as a variable:

    player_tag = "YOUR_PLAYER_TAG"
   it is also important to mention here that you should not include the hashtag in the variable. the request uses %23 in place of the hashtag so it has been added already. Failure to remove this will result in a 404 error.
   
