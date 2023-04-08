import datetime
import discord
from redbot.core import commands

class MyCog(commands.Cog):
    """MuteManager"""
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    @commands.checks.has_permissions(moderate_members=True)
    async def mute(ctx, member: discord.Member, time, reason):
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
