import discord
from discord import Member
from discord import Status
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure
from collections import Counter
from discord.utils import get


bot = commands.Bot(command_prefix="=")
bot.remove_command('help')

@bot.event
async def on_ready():
    print("Bot ist bereit")



@bot.command(pass_context=True)
async def join(ctx, channel: discord.Channel):
        await bot.send_message(ctx.message.channel, 'لا')
        msg = await bot.wait_for_message(author=ctx.message.author, content='باليز')
        await bot.send_message(ctx.message.channel, 'لا')
        msg = await bot.wait_for_message(author=ctx.message.author, content='باليز')
        await bot.send_message(ctx.message.channel, 'لا')
        msg = await bot.wait_for_message(author=ctx.message.author, content='باليز')     
        await bot.send_message(ctx.message.channel, 'K')                   
        await bot.join_voice_channel(channel)



bot.run(str(os.environ.get('BOT_TOKEN')))
