import discord
from discord.ext import commands
from Discord_Bot.core.classes import Cog_Extension
import json

with open('setting.json', 'r', encoding='utf8') as jFile:
    jdata = json.load(jFile)

class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(F'{member} 加入群組')
        channel = self.bot.get_channel(int(jdata['test_channel']))
        await channel.send(F'{member} 加入群組！')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(F'{member} 離開群組')
        channel = self.bot.get_channel(int(jdata['test_channel']))
        await channel.send(F'{member} 離開群組！')
    
    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.content in jdata['keyword'] and msg.author != self.bot.user:
            await msg.channel.send('Test By : ' + str(msg.author) + " (" + str(msg.author.id)+ ")")

def setup(bot):
    bot.add_cog(Event(bot))