import os
import discord
import asyncio
import configparser
from bot.commands import Command

client = discord.Client()


@client.event
@asyncio.coroutine
def on_ready():
    print('Logged in as: {0} - {1}'.format(client.user.name, client.user.id))
    print('-'*20)


@client.event
@asyncio.coroutine
def on_message(message):
    command = message.content.lower()
    if message.author == client.user:
        return
    elif command == '!':
        yield from client.send_message(message.channel, '<@{0}>, No command has been passed.'.format(message.author.id))
    elif command.startswith('!leet'):
        response = Command.leet_speak(command.replace('!leet', ''))
        yield from client.send_message(message.channel, '{0}'.format(response))


# Set up the base bot
class DiscordBot(object):
    def __init__(self):
        self.token = None

    def set_token(self):
        # Check if BOT_TOKEN os var exists
        if os.getenv('BOT_TOKEN') is not None:
            self.token = os.getenv('BOT_TOKEN')
            print('Using bot token from environment file')
        else:
            # Ask user for bot token
            self.token = input('Bot Token:')

    def run(self):
        client.run(self.token)
