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

    @commands.command()
    async def resay(self, ctx, *, msg):
        await ctx.message.delete()
        await ctx.send(msg)

    @commands.command()
    async def cmsg(self, ctx, num : int):
        await ctx.channel.purge(limit = num+1)


#註冊Cog
def setup(bot):
    bot.add_cog(Main(bot))