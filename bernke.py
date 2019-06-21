"""
Justin Stachofsky
bernke.py
Created: 2/12/2019
Last Edit: 2/12/2019

Bot for Tragedy of the Commons Discord Server
Written poorly on purpose I swear.
"""

import discord
import asyncio
import random

# Stores token information
import config

bot_token = config.bot_token
client = discord.Client()
r = random.SystemRandom()

@client.event
@asyncio.coroutine
def on_message(message):

    # Rat react any posts in the rat zone channel
    if str(message.channel) == "rat-zone-memorial-breakfast":
        yield from client.add_reaction(message, "\U0001F400")
   
    # Prevent infinite loop
    if message.author == client.user:
        return   

    # Awful if statement for bot commands
    if message.content.startswith('!everyone'):
        msg = '@everyone lmao'.format(message)
        yield from client.send_message(message.channel, msg)
    elif message.content.startswith('!takerate'):
        rate = 'Q' + str(r.randint(1,4)) + ' Take'
        msg = rate.format(message)
        yield from client.send_message(message.channel, msg)
    elif message.content.startswith('!takematrix'):
        msg = 'Q1 = Hot and Right, Q2 = Hot and Wrong, Q3 = Cold and Wrong, Q4 = Cold and Right'.format(message)
        yield from client.send_message(message.channel, msg)
    elif message.content.startswith('!thisi'):
        msg = 'This, but ironically'.format(message)
        yield from client.send_message(message.channel, msg)
    elif message.content.startswith('!thisu'):
        msg = 'This, but unironically'.format(message)
        yield from client.send_message(message.channel, msg)
    elif message.content.startswith('!child'):
        msg = 'Did a child write this?'.format(message)
        yield from client.send_message(message.channel, msg)
    elif message.content.startswith('!model'):
        msg = "What's your model?".format(message)
        yield from client.send_message(message.channel, msg)
    elif message.content.startswith('!failure'):
        msg = '{0.author.mention} is a market failure'.format(message)
        yield from client.send_message(message.channel, msg)
    elif message.content.startswith('!balls'):
        msg = 'Do it no balls'.format(message)
        yield from client.send_message(message.channel, msg)
    elif 'bitcoin' in message.content:
        msg = '>bitcoin. lmao nice meme'.format(message)
        yield from client.send_message(message.channel, msg, tts=True)
    elif 'stupid' in message.content:
        msg = discord.Embed()
        msg.set_image(url="https://i.imgur.com/LFIi7yS.jpg")
        yield from client.send_message(message.channel, embed=msg)
    elif message.content.startswith('!god'):
        msg = discord.Embed()
        msg.set_image(url="https://i.imgur.com/pZi485H.jpg")
        yield from client.send_message(message.channel, embed=msg)
    elif message.content.startswith('!GOD'):
        msg = discord.Embed()
        msg.set_image(url="https://i.imgur.com/VKqSxBH.jpg")
        yield from client.send_message(message.channel, embed=msg)
    elif message.content.startswith('!dumbdumb'):
        msg = 'lol ur big dumb'.format(message)
        yield from client.send_message(message.channel, embed=msg)
    elif message.content.startswith('!specifictakerate'):
        msg = '(' + str(r.randint(-999999999,999999999)) + ', ' + str(r.randint(-999999999,999999999)) + ') Use !takerate for a more general take'.format(message)
        yield from client.send_message(message.channel, msg)
    elif message.content.startswith('!census'):
        msg = 'https://www2.census.gov/library/publications/decennial/1860/population/1860a-31.pdf'
        yield from client.send_message(message.channel, msg)
    elif message.content.startswith('!iconic'):
        msg = discord.Embed()
        msg.set_image(url="https://i.imgur.com/k7FjY1m.jpg")
        yield from client.send_message(message.channel, embed=msg)
    elif message.content.startswith('!git'):
        msg = 'git commit -m "no need for pull request already reviewed changes dw"\ngit push origin master'
        yield from client.send_message(message.channel, msg)
    elif 'ethereum' in message.content:
        msg = '>ethereum. lmao nice meme'.format(message)
        yield from client.send_message(message.channel, msg, tts=True)
    elif message.content.startswith('!value'):
        msg = 'https://www.youtube.com/watch?v=WnPjqt6vEzA'.format(message)
        yield from client.send_message(message.channel, msg)
    elif message.content.startswith('!trailer'):
        msg = 'https://youtu.be/z7-LxU4SqCw'.format(message)
        yield from client.send_message(message.channel, msg)

@client.event
@asyncio.coroutine
def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(bot_token)

