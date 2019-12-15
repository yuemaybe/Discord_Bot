import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('機器人測試上線')

@bot.event
async def on_member_join(member):
    print(F'{member} 加入群組')
    channel = bot.get_channel(654717730800533531)
    await channel.send(F'{member} 加入群組！')

@bot.event
async def on_member_remove(member):
    print(F'{member} 離開群組')
    channel = bot.get_channel(654717730800533531)
    await channel.send(F'{member} 離開群組！')

bot.run('NjU0NzE4Nzg3MDI2NjgxODY2.XfJtog.MJCPfCkTFJNoWFQTy5BPHbaB2as')







