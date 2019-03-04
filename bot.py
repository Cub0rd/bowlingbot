import asyncio
import discord
import youtube_dl
from discord.ext import commands
import datetime
import time
import random
from multiprocessing import Process


started = 0

client = commands.Bot(command_prefix = '.')


@client.event
async def on_ready():
    global started
    if started == 0:
        print('\n')
        print('Bot online as:')
        print(client.user.name)
        print(client.user.id)
        await client.change_presence(game=discord.Game(name='at the bowling alley.'))
        print('\n')
        started = 1


@client.command(pass_context=True)
async def bowl(ctx):

    if 'Ball' in client.user.name and not client.is_voice_connected(ctx.message.server) and ctx.message.author.voice_channel != None:
        voice = await client.join_voice_channel(ctx.message.author.voice_channel)
        
        await client.say(ctx.message.author.mention + ' is throwing the ball...')
        time.sleep(2)

        score = int(random.randint(0,10))
        
        if score > 0:
            player = voice.create_ffmpeg_player('bowling.wav')
        else:
            player = voice.create_ffmpeg_player('gutter.wav')
        player.start()
        while not player.is_done():
            asyncio.sleep(1)
        player.stop()

        if score == 0:
            await client.say(ctx.message.author.mention + ' Oof, it\'s a gutter!')
        elif score == 10:
            await client.say(ctx.message.author.mention + ' got a strike!')
        elif score == 1:
            await client.say(ctx.message.author.mention + ' knocked down 1 pin.')
        else:
            await client.say(ctx.message.author.mention + ' knocked down ' + str(score) + ' pins.')
        time.sleep(1)

        await voice.disconnect()

        

    if 'Pin' in client.user.name and not client.is_voice_connected(ctx.message.server):
        await client.wait_for_message(author=ctx.message.server.get_member('546738252455870509'), timeout=4)
        time.sleep(random.uniform(0, 1.5))
        voice = await client.join_voice_channel(ctx.message.author.voice_channel)
        await client.wait_for_message(author=ctx.message.server.get_member('546738252455870509'))
        time.sleep(random.uniform(0, 1))
        await voice.disconnect()

    





def ball():
    client.run('TOKEN1')
def pin1():
    client.run('TOKEN2')
def pin2():
    client.run('TOKEN3')
def pin3():
    client.run('TOKEN4')
def pin4():
    client.run('TOKEN5')
def pin5():
    client.run('TOKEN6')
def pin6():
    client.run('TOKEN7')
def pin7():
    client.run('TOKEN8')
def pin8():
    client.run('TOKEN9')
def pin9():
    client.run('TOKEN10')
def pin0():
    client.run('TOKEN11')



one = Process (target=ball)
two = Process (target=pin1)
three = Process(target=pin2)
four = Process (target=pin3)
five = Process(target=pin4)
six = Process (target=pin5)
seven = Process(target=pin6)
eight = Process (target=pin7)
nine = Process(target=pin8)
ten = Process (target=pin9)
eleven = Process(target=pin0)

delay = 0.1

one.start()
time.sleep(delay)
two.start()
time.sleep(delay)
three.start()
time.sleep(delay)
four.start()
time.sleep(delay)
five.start()
time.sleep(delay)
six.start()
time.sleep(delay)
seven.start()
time.sleep(delay)
eight.start()
time.sleep(delay)
nine.start()
time.sleep(delay)
ten.start()
time.sleep(delay)
eleven.start()
time.sleep(delay)
