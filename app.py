import os
from bot.bot import DiscordBot

if __name__ == '__main__':

    bot = DiscordBot()

    # set discord bot token from environment var or user input
    bot.set_token()

    bot.run()
