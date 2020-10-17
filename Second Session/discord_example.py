# Make a program that listens to messages in a channel and prints them in console for recording use

import discord

client = discord.Client()

@client.event
async def on_ready():
	print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
	if message.author == client.user:
		return
	await message.channel.send("Hello!")

client.run("NzYyMzU3MjE4OTcyNTMyNzY4.X3n-fA.Vmzvp1_BDNzL8orE_KXgEvHumuw")
