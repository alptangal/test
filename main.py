import asyncio
import os
import re,json
import discord
from discord.ext import commands, tasks
from discord import app_commands
from discord.utils import get
import random
from datetime import datetime,timedelta


intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
VIETTELS='032, 033, 034, 035, 036, 037, 038, 039, 096, 097, 098, 086'
VIETTELS=VIETTELS.split(',')
VINAPHONES=' 091, 094, 088, 081, 082, 083, 084, 085'
VINAPHONES=VINAPHONES.split(',')
VIETNAMOBILE='052, 056, 058, 092'
VIETNAMOBILE=VIETNAMOBILE.split(',')
HEADERS = []
THREADS = []
USERNAMES = [] 
GUILDID = 1122707918177960047 
RESULT=1
#server.b()
@client.event
async def on_ready():
    if not taskKeepCookie.is_running():
      taskKeepCookie.start(guild)
@tasks.loop(seconds=1)
async def taskKeepCookie(guild):
  global RESULT
  RESULT=await getBasic(guild)
client.run(st.secrets["botToken"])
