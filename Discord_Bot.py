import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix = '')

@client.event

async def on_ready():
    print('Bot is Ready.')


@client.command(aliases=['wtf', 'hey']) #anything put under the list for aliases will trigger this command.
async def messages(ctx):
    responses = ['Fuck Off',
    'Eat Shit']
    await ctx.send(f'{random.choice(responses)}')
            

client.run('Discord Bot Token Here')