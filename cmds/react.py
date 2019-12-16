import discord
from discord.ext import commands
from Discord_Bot.core.classes import Cog_Extension
import random
import json
import datetime
import pytz

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

    @commands.command()
    async def 開發(self, ctx):
        tw = pytz.timezone('Asia/Taipei')
        embed=discord.Embed(title="Enbed測試器", url="https://www.google.com.tw/", description="測試用", color=0x00ff00, 
        timestamp=datetime.datetime.now(tw))
        embed.set_author(name="YG123", url="https://memes.tw/user-resource/e00b71581ce7bba48278700ed77f7a42.png", icon_url="https://memes.tw/user-resource/e00b71581ce7bba48278700ed77f7a42.png")
        embed.set_thumbnail(url="https://memes.tw/user-resource/6ec00f197961fdd0b6398b102b9f529e.png")
        embed.add_field(name="開發環境", value="Python", inline=True)
        embed.add_field(name="開發工具", value="VScode", inline=True)
        embed.set_footer(text="By YG")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(React(bot))