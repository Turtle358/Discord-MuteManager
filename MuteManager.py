import discord
from discord import Option
from datetime import timedelta
from discord.ext import commands
from discord.ext.commands import MissingPermissions

bot = discord.Bot()
servers = [1065179832369020959]
@bot.event
async def on_ready():
    print(f'You have logged in as {bot.user}')

@bot.slash_command(guild_ids = servers, name = 'mute', description = "mutes/timeouts a member")
@commands.has_permissions(moderate_members = True)
async def mute(ctx, member: Option(discord.Member, required = True), reason: Option(str, required = False), days: Option(int, max_value = 27, default = 0, required = False), hours: Option(int, default = 0, required = False), minutes: Option(int, default = 0, required = False), seconds: Option(int, default = 0, required = False)):
    if member.id == ctx.author.id:
        await ctx.respond("You can't timeout yourself!", ephemeral = True)
        return
    if member.guild_permissions.moderate_members:
        await ctx.respond("You can't do this, this person is a moderator!", ephemeral = True)
        return
    duration = timedelta(days = days, hours = hours, minutes = minutes, seconds = seconds)
    if duration >= timedelta(days = 28):
        await ctx.respond("I can't mute someone for more than 28 days!", ephemeral = True)
        return
    if reason == None:
        await member.timeout_for(duration)
        await ctx.respond(f"<@{member.id}> has been timed out for {days} days, {hours} hours, {minutes} minutes, and {seconds} seconds by <@{ctx.author.id}>.", ephemeral = True)
        await member.send(f"<@{member.id}> has been timed out for {days} days, {hours} hours, {minutes} minutes, and {seconds} seconds by .")
        modchannel = bot.get_channel(1074398747473215569)
        await modchannel.send(f"<@{member.id}> has been timed out for {days} days, {hours} hours, {minutes} minutes, and {seconds} seconds by <@{ctx.author.id}>.")
    else:
        await member.timeout_for(duration, reason = reason)
        await ctx.respond(f"<@{member.id}> has been timed out for {days} days, {hours} hours, {minutes} minutes, and {seconds} seconds by <@{ctx.author.id}> for '{reason}'.", ephemeral = True)
        await member.send(f"<@{member.id}> has been timed out for {days} days, {hours} hours, {minutes} minutes, and {seconds} seconds by for '{reason}'.")
        modchannel = bot.get_channel(1074398747473215569)
        await modchannel.send(f"<@{member.id}> has been timed out for {days} days, {hours} hours, {minutes} minutes, and {seconds} seconds by <@{ctx.author.id}> for '{reason}'.")

@mute.error
async def timeouterror(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.respond("You can't do this! You need to have moderate members permissions!", ephemeral = True)
    else:
        raise error
@bot.slash_command(guild_ids=servers, name = "say", decription="Say command")
@commands.has_permissions(moderate_members=True)
async def say(ctx, message: Option(str,required=True)):
    try:
        await ctx.send(message)
        await ctx.respond("Message sent", ephemeral = True)
    except:
        await ctx.respond("An error occured", ephemeral=True )


bot.run("ACCESS-TOKEN")
