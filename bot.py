import discord
from discord import Member
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure
import requests

Prefix = "-" # BOT PREFIX
bot = commands.Bot(command_prefix=Prefix)
antibot = True
 
@bot.event
async def on_ready():
    print("Im Online Bro {}".format(len(bot.servers)))

@bot.event
async def on_member_join(member):
    if antibot is True:
        if member.bot == True:
            logs = discord.utils.get(member.server.channels, name="logs")
            await bot.ban(member)
            await bot.send_message(logs, f"{member.name} with id {member.id} has banned by bot < antibot > !")
        if member.bot == False:
            channel = discord.utils.get(member.server.channels, name="welcome")
            await bot.send_message(channel, f"{member} Welcome To {member.server.name}")    


@bot.group(pass_context=True)
async def antibot(ctx):
    if ctx.invoked_subcommand == None:
        await bot.send_message(ctx.message.channel, f"{Prefix}antibot on | On Bot Join Will Ban Him !\n{Prefix}antibot off | On Bot Join Will Get Welcome Channel And Send Message To Channel < BOT Welcome To ServerName > ")
@antibot.command(pass_context=True)
async def on(ctx):
    global antibot
    antibot = True
    await bot.say("AntiBot Is On !")

@antibot.command(pass_context=True)
async def off(ctx):
    global antibot
    antibot = False
    await bot.say("AntiBot Is Off !")


bot.run(str(os.environ.get('BOT_TOKEN')))
