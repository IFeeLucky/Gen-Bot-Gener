import discord, datetime, asyncio, os
from datetime import datetime
from discord.ext import commands
from pystyle import Colors, Colorate

Funny = commands.Bot(command_prefix='$', self_bot=True)

genmsg = '.nfa'
channel_id = 923979100140474378
bot_id = 791694664159199253
token = "yout token here"
if not os.path.isfile('alts.txt'):
    f = open('alts.txt', "w", encoding="UTF-8")
    f.write("")
    f.close()
if not os.path.isfile('trash.txt'):
    f = open('trash.txt', "w", encoding="UTF-8")
    f.write("")
    f.close()
@Funny.event
async def on_message(message):
    if message.channel.type is discord.ChannelType.private:
        if message.author.id == bot_id:
            print(Colorate.Color(Colors.dark_green, 'Message Recieved'))
            try:
                embed = message.embeds[0].to_dict()
                desc = embed["description"]
            except:
                desc = "No embed"
                pass
            if ':' in message.content:
                alt = message.content
                print(Colorate.Color(Colors.dark_green, 'New alt recieved!') + f"[{alt}] | [{datetime.now().strftime('%H:%M')}]")
                with open('alts.txt', 'a', encoding="utf-8") as file:
                    file.write(alt + '\n')
                    file.close()
            elif ':' in desc:
                alt = desc
                print(Colorate.Color(Colors.dark_green, 'New alt recieved!') + f"[{alt}] | [{datetime.now().strftime('%H:%M')}]")
                with open('alts.txt', 'a', encoding="utf-8") as file:
                    file.write(alt + '\n')
                    file.close()
            else:
                with open('trash.txt', 'a', encoding="utf-8") as file:
                    file.write(message.content + " | " + desc + '\n')
                    file.close()
    await Funny.process_commands(message)

@Funny.event
async def on_connect():
    os.system('cls')
    print(f"Bot ready")
    while True:
        channel = Funny.get_channel(channel_id)
        await channel.send(genmsg)
        print(Colorate.Color(Colors.dark_green, f'{genmsg} sent!'))
        await asyncio.sleep(3600)

    

@Funny.command()
async def beat(ctx):
    await ctx.send('online')



Funny.run(token)

# Lukie Bets koder!!!?!?!?