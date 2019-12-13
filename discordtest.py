#!/usr/bin/env python
# coding: utf-8

# In[4]:


import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('機器人測試上線')
    
bot.run('NjU0NzE4Nzg3MDI2NjgxODY2.XfJtog.MJCPfCkTFJNoWFQTy5BPHbaB2as')


# In[ ]:




