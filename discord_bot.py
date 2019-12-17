import discord
from discord.ext import commands
import json
import random
import os

#開啟檔案
with open('setting.json', 'r', encoding='utf8') as jFile:
    jdata = json.load(jFile)

#機器人指令開頭
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('機器人測試上線')
    channel = bot.get_channel(int(jdata['test_channel']))
    await channel.send('機器人已上線  :100:')

@bot.command()
async def close(ctx):
    print('機器人測試離線')
    await ctx.send('機器人已離線  :skull:')
    await bot.close()

@bot.command()
async def load(ctx, extension):
    bot.load_extension(F'cmds.{extension}')
    await ctx.send(F'載入 {extension} 完畢')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(F'cmds.{extension}')
    await ctx.send(F'卸載 {extension} 完畢')

@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(F'cmds.{extension}')
    await ctx.send(F'重載 {extension} 完畢')

for Filename in os.listdir('./cmds'):
    if Filename.endswith('.py'):
        bot.load_extension(F'cmds.{Filename[:-3]}')

if __name__ == "__main__":
    bot.run(jdata['TOKEN'])







