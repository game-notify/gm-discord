import os
import discord
import asyncio
from bot.commands import Command

client = discord.Client()


@client.event
@asyncio.coroutine
def on_ready():
    print('Logged in as: {0} - {1}'.format(client.user.name, client.user.id))
    print('-'*20)

def gen_embed(offers):
    embed = discord.Embed(
        title='TOP 10 game offers',
        url='https://github.com/game-notify/gm-discord'
        )
    for provider in offers:
        embed.add_field(name=provider['name'], value='\u200b')
        embed.add_field(name='\u200b', value='\u200b')
        embed.add_field(name='\u200b', value='\u200b')
        for offer in provider['offers']:
            embed.add_field(name=offer['title'], value=f'{offer["newPrice"]} [Purchase]({offer["url"]})')
        # tmp while implementing steam apis
        embed.add_field(name='\u200b', value='\u200b')
        embed.add_field(name='\u200b', value='\u200b')
        embed.add_field(name='\u200b', value='\u200b')

        embed.add_field(name='Steam', value='Comming soon')
    embed.set_footer(text='')

    return embed


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
