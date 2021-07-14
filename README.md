# ETSIINF Bus Bot
This is a very basic telegram bot that gives you bus times on different stations (just thinking about the students at the ETSIINF-UPM University of Madrid)

Telegram name: @theNewEtsiinfBot

# Stops Included
- 08771: 
  * Buses: 566, 571, 573
  * Street: TODO
- 08411:
  * Buses: 591
  * Street: TODO
- 17573:
  * Buses: 865
  * Street: TODO
- 08409:
  * Buses: 571, 573, 591
  * Street: TODO
- 15782:
  * Buses: 571
  * Street: TODO
- 08380:
  * Buses: 591
  * Street: TODO
- 11278:
  * Buses: 573, 865
  * Street: TODO

# Deploy

First install (I'm using python 3.9.6 and pip 20.3.4):
```console
pip install python-telegram-bot requests
```

Then create a new BOT with BotFather (@BotFather) on Telegram. After getting a token create an environment variable like this:
```console
export etsiinfBOT="YOUR-SUPER-TOKEN"
```
I have this line on my `.zshrc` file. 

Finally run `python view.py`
And done :D now chat with your bot from telegram.

# Docker

Create a new BOT with BotFather (@BotFather) on Telegram. After getting a token create an environment variable like this:
```console
export etsiinfBOT="YOUR-SUPER-TOKEN"
```
I have this line on my `.zshrc` file. 

Now, create and execute the docker as follows:
```console
docker build -t etsiinf-bot .
docker run -e etsiinfBOT=$etsiinfBOT etsiinf-bot
```

And done :D now chat with your bot from telegram.
