
from bot.bot import DiscordBot
from dotenv import load_dotenv


if __name__ == '__main__':

    load_dotenv()
    bot = DiscordBot()

    # set discord bot token from environment var or user input
    bot.set_token()

    bot.run()
