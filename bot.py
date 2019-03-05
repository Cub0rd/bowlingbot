import asyncio
import discord
from discord.ext import commands
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

score = None

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
            await client.say(ctx.message.author.mention + " Oof, it's a gutter! Type `finish` to finish.")
        elif score == 10:
            await client.say(ctx.message.author.mention + ' got a strike!')
        elif score == 1:
                await client.say(ctx.message.author.mention + ' knocked down 1 pin. Type `finish` to finish.')
        else:
            await client.say(ctx.message.author.mention + ' knocked down ' + str(score) + ' pins. Type `finish` to finish.')
        
        if score < 10:
            remaining = 10 - score
            new_score = int(random.randint(0, remaining))
            finish = await client.wait_for_message(author=ctx.message.author, timeout=15, content='finish')
            if finish != None:
                await client.say(ctx.message.author.mention + ' is throwing the ball for the second time...')
                time.sleep(2)
                if new_score > 0:
                    player = voice.create_ffmpeg_player('bowling.wav')
                else:
                    player = voice.create_ffmpeg_player('gutter.wav')
                player.start()
                while not player.is_done():
                    asyncio.sleep(1)
                player.stop()

                final_score = score + new_score

                if final_score == 0:
                    await client.say(ctx.message.author.mention + ' Oof, it\'s a gutter again!')
                elif final_score == 10:
                    await client.say(ctx.message.author.mention + ' got a spare!')
                elif new_score == 1:
                    await client.say(ctx.message.author.mention + ' knocked down ' + str(new_score) + ' pin, making ' + str(final_score) + ' their final score.')
                else:
                    await client.say(ctx.message.author.mention + ' knocked down ' + str(new_score) + ' pins, making ' + str(final_score) + ' their final score.')


        time.sleep(1)

        await voice.disconnect()

    if 'Pin' in client.user.name and not client.is_voice_connected(ctx.message.server):

        pin_ids= ['BOWLINGPIN_1_USER_ID', 'BOWLINGPIN_2_USER_ID', 'BOWLINGPIN_3_USER_ID', 'BOWLINGPIN_4_USER_ID', 'BOWLINGPIN_5_USER_ID', 'BOWLINGPIN_6_USER_ID', 'BOWLINGPIN_7_USER_ID', 'BOWLINGPIN_8_USER_ID', 'BOWLINGPIN_9_USER_ID', 'BOWLINGPIN_10_USER_ID']

        count = 1
        for pin_id in pin_ids:
            if pin_id == client.user.id:
                pin_number = count
            count +=1
        
        await client.wait_for_message(author=ctx.message.server.get_member('BOWLING_BALL_USER_ID'), timeout=4)
        time.sleep(random.uniform(0, 1.5))
        voice = await client.join_voice_channel(ctx.message.author.voice_channel)
        
        message = await client.wait_for_message(author=ctx.message.server.get_member('BOWLING_BALL_USER_ID'))
        time.sleep(1)
        if 'gutter' in message.content:
            pins_left = 10
        elif '1 pin' in message.content:
            pins_left = 9
        elif '2 pins' in message.content:
            pins_left = 8
        elif '3 pins' in message.content:
            pins_left = 7
        elif '4 pins' in message.content:
            pins_left = 6
        elif '5 pins' in message.content:
            pins_left = 5
        elif '6 pins' in message.content:
            pins_left = 4
        elif '7 pins' in message.content:
            pins_left = 3
        elif '8 pins' in message.content:
            pins_left = 2
        elif '9 pins' in message.content:
            pins_left = 1
        elif 'strike' in message.content:
            pins_left = 0

        if pins_left == 0:
            time.sleep(random.uniform(0, 0.5))
            await voice.disconnect()

        elif pin_number <= pins_left:

            rebowl = await client.wait_for_message(author=ctx.message.author, timeout=15, content='rebowl')

            if rebowl != None:
                await client.wait_for_message(author=ctx.message.server.get_member('BOWLING_BALL_USER_ID'))
                await client.wait_for_message(author=ctx.message.server.get_member('BOWLING_BALL_USER_ID'))
            time.sleep(random.uniform(0, 0.5))
            await voice.disconnect()

        else:
            time.sleep(random.uniform(0, 0.5))
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

one = Process(target=ball)
two = Process(target=pin1)
three = Process(target=pin2)
four = Process(target=pin3)
five = Process(target=pin4)
six = Process(target=pin5)
seven = Process(target=pin6)
eight = Process(target=pin7)
nine = Process(target=pin8)
ten = Process(target=pin9)
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
