import discord
import psutil
import time
from pypresence import Presence
from discord.ext import commands
    
client = commands.Bot('.', self_bot = False)

TOKEN = ''

client_id = ''
RPC = Presence(client_id)
RPC.connect()

while True:
	cpu_per = round(psutil.cpu_percent(),1)
	mem = psutil.virtual_memory()
	mem_per = round(psutil.virtual_memory().percent,1)
	ping = round(client.latency, 1)
	RPC.update(details='CPU: '+str(cpu_per)+ '% ' 'RAM: '+str(mem_per)+ '%')
	time.sleep(1)
	
client.run(TOKEN, bot=False)