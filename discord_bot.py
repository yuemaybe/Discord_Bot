import discord
from discord.ext import commands
import json
import random

with open('setting.json', 'r', encoding='utf8') as jFile:
    jdata = json.load(jFile)


bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('機器人測試上線')
    channel = bot.get_channel(int(jdata['test_channel']))
    await channel.send('機器人已上線  :100:')

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
async def 圖片(ctx):
    pic = discord.File(jdata['pic'])
    await ctx.send(file=pic)

@bot.command()
async def 隨機(ctx):
    rr = random.choice(jdata['rpic'])
    rpic = discord.File(rr)
    await ctx.send(file=rpic)

@bot.command()
async def 圖片2(ctx):
    await ctx.send(jdata['pic_url'])




bot.run(jdata['TOKEN'])







