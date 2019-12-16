import discord
from discord.ext import commands
from Discord_Bot.core.classes import Cog_Extension
import random
import json

with open('setting.json', 'r', encoding='utf8') as jFile:
    jdata = json.load(jFile)

class React(Cog_Extension):
    
    @commands.command()
    async def 圖片(self, ctx):
        pic = discord.File(jdata['pic'])
        await ctx.send(file=pic)

    @commands.command()
    async def 隨機(self, ctx):
        rr = random.choice(jdata['rpic'])
        rpic = discord.File(rr)
        await ctx.send(file=rpic)

    @commands.command()
    async def web(self, ctx):
        await ctx.send(jdata['pic_url'])

def setup(bot):
    bot.add_cog(React(bot))