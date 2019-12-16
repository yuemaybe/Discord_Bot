import discord
from discord.ext import commands
from Discord_Bot.core.classes import Cog_Extension

#從classes.py繼承Cog_Extension使用
class Main(Cog_Extension):

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(F'{round(self.bot.latency * 1000)} ms')
    
    @commands.command()
    async def test(self, ctx):
        await ctx.send('test123')

#建置機器人
def setup(bot):
    bot.add_cog(Main(bot))