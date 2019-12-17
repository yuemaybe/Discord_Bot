import discord
from discord.ext import commands
from Discord_Bot.core.classes import Cog_Extension
import asyncio, asyncio, datetime, json

with open('setting.json', 'r', encoding='utf8') as jFile:
    jdata = json.load(jFile)

class Task(Cog_Extension):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        async def interval():
            await self.bot.wait_until_ready()
            self.channel = self.bot.get_channel(int(jdata['test_channel']))
            while not self.bot.is_closed():
                await self.channel.send('執行中 (5s)')
                await asyncio.sleep(5) # 暫停 5 秒
        
        self.bg_task = self.bot.loop.create_task(interval())

    @commands.command()
    async def 換頻(self, ctx, ch : int):
        self.channel = self.bot.get_channel(ch)
        await ctx.send(F'目前頻道 : {self.channel.mention}')







def setup(bot):
    bot.add_cog(Task(bot))