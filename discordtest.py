import discord
from discord.ext import commands
import json

with open('setting.json', 'r', encoding='utf8') as jFile:
    jdata = json.load(jFile)


bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('機器人測試上線')
    channel = bot.get_channel(int(jdata['test_channel']))
    # await channel.send('機器人已上線  :100:')

@bot.event
async def on_member_join(member):
    print(F'{member} 加入群組')
    channel = bot.get_channel(int(jdata['test_channel']))
    await channel.send(F'{member} 加入群組！')

@bot.event
async def on_member_remove(member):
    print(F'{member} 離開群組')
    channel = bot.get_channel(int(jdata['test_channel']))
    await channel.send(F'{member} 離開群組！')

@bot.command()
async def ping(ctx):
    await ctx.send(F'{round(bot.latency * 1000)} ms')

@bot.command()
async def test(ctx):
    pic = discord.File('C:\\Users\\yuema\\OneDrive\\文件\\GitHub\\Discord_Bot\\pic\\2.jpg')
    await ctx.send(File = pic)




bot.run(jdata['TOKEN'])







