import datetime
import discord
from redbot.core import commands

class MyCog(commands.Cog):
    """DiscordMuteManager"""
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def mute(ctx, member: discord.Member, time, reason):
        if not ctx.message.author.server_permissions.administrator:
            await ctx.channel.send("You cannot mute people")
        if ctx.message.author == member.id:
            await ctx.channel.send("You cannot mute youself")
        if ctx.message.author.server_permissions.administrator or ctx.message.author.id == 560181647006367794:
            if "h" in time:
                time.replace("h","")
                print(time)
                await member.timeout(until=datetime.timedelta(hours=time), reason=reason)
                await member.send(f"You have been muted for {time}hours, with the reason: `{reason}`")
            if "d" in time:
                time.replace("d","")
                print(time)
                await member.timeout(until=datetime.timedelta(hours=time), reason=reason)
                await member.send(f"You have been mute for {time}days with the reason: `{reason}`")
            embed = discord.Embed(title=f":white_check_mark: {member.name} has been successfully muted")
            await ctx.send(embed=embed)