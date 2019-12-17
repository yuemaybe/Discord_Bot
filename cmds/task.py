import discord
from discord.ext import commands
from Discord_Bot.core.classes import Cog_Extension
import asyncio, asyncio, datetime, json

with open('setting.json', 'r', encoding='utf8') as jFile:
    jdata = json.load(jFile)

class Task(Cog_Extension):
    def __init__(self, *args, **kwargs): #任務需要寫在init底下，其他則不用。
        super().__init__(*args, **kwargs)

        self.counter = 0

        # async def interval():
        #     await self.bot.wait_until_ready()
        #     self.channel = self.bot.get_channel(int(jdata['test_channel']))
        #     while not self.bot.is_closed():
        #         await self.channel.send('執行中 (100s)')
        #         await asyncio.sleep(100) # 暫停 5 秒
        
        # self.bg_task = self.bot.loop.create_task(interval())


        async def time_task():
            await self.bot.wait_until_ready()
            with open('setting.json', 'r', encoding='utf8') as jFile:
                jdata = json.load(jFile)
            self.channel = self.bot.get_channel(int(jdata['test_channel']))
            while not self.bot.is_closed():
                now_time = datetime.datetime.now().strftime('%H%M')

                with open('setting.json', 'r', encoding='utf8') as jFile:
                    jdata = json.load(jFile)

                if (now_time == jdata['time'] and self.counter == 0):
                    self.counter = 1
                    await self.channel.send('測試中')
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
                    pass
        self.t_task = self.bot.loop.create_task(time_task())

    @commands.command()
    async def settime(self, ctx, time):
        self.counter = 0
        with open('setting.json', 'r', encoding='utf8') as jFile:
            jdata = json.load(jFile)
        jdata['time'] = time
        with open('setting.json','w',encoding='utf8') as jwfile:
            json.dump(jdata, jwfile, indent=4)


def setup(bot):
    bot.add_cog(Task(bot))