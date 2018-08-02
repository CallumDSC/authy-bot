# Importing Modules

import os
import time
import random
import discord
import re
from discord.ext import commands
from time import sleep
import discord.utils
from discord.utils import get
import traceback

# System Information

client = commands.Bot(command_prefix = "a!")
client.remove_command("help")
client.Version = '0.9 - Beta'
client.Author = 'Callum.#3955'
client.Token = 'bot token'
client.Oauth2 = 'https://discordapp.com/oauth2/authorize?client_id=472920271326543872&scope=bot&permissions=2146958591'
client.InsufficientPermissions = 'You have insufficient permissions to perform this command.'

# System Activation

@client.event
async def on_ready():
    print(f"Success! The bot is active and is running on Version {client.Version}!")
    print("--------------------------------------------------------------------")
    print(f"To invite the bot to your server, use the invite link - {client.Oauth2}")

# Information Commands

@commands.cooldown(1, 10, commands.BucketType.user)
@client.command(pass_context = True)
async def help():
    embed = discord.Embed(colour=0x80FF33)
    embed = discord.Embed(title=f"__Authy Manual | {client.Version}__", color=0x2EFF00)
    embed.add_field(name="Developer Commands", value="Bot developers do not have access to their own commands, however, eval may be added in order to debug problems without having to restart the bot entirely.")
    embed.add_field(name="Information Commands", value="a!help - This command displays this manual.")
    embed.add_field(name="Moderation Commands", value="a!kick - Kicks a user from the server.\na!ban - Bans a user from the server.")
    embed.add_field(name="General Commands", value="a!help - This command displays this manual.")
    embed.set_footer(text=f"Authy™ • Created by {client.Author}")
    await client.say(embed=embed)

# Moderation Commands

@commands.cooldown(1, 10, commands.BucketType.user)
@client.command(pass_context = True) 
async def kick(ctx, member: discord.Member=None, reason: str=None):
  if ctx.message.author.server_permissions.kick_members:
   if not member or not reason:
    embed = discord.Embed(colour=0xED3F3F, title="Command: a!kick", description="**Category**: Moderation Commands\n**Description**: Kicks X user.\n**Cooldown**: 3 seconds\n**Usage**: a!kick <@user> <reason> \n**Example**: a!kick @Callum#8593 Excessive spamming.")
    await client.say(embed=embed)
   else:
    await client.kick(member)
    await client.say(f"{member.mention} Has been kicked from the server for \"{reason}")
  else:
    await client.say(f"client.InsufficientPermissions")

client.run(client.Token)
