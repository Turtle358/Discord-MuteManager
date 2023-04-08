import datetime
from discord import app_commands
from redbot.core import commands

class MyCog(commands.Cog):
    """MuteManager"""
    def __init__(self, bot):
        self.bot = bot
    @app_commands.command(name='timeout', description='timeouts a user for a specific time')
    @app_commands.checks.has_permissions(moderate_members=True)
    async def timeout(self, interaction: Interaction, member: Member, seconds: int = 0, minutes: int = 0,
                      hours: int = 0, days: int = 0, reason: str = None):
        duration = datetime.timedelta(seconds=seconds, minutes=minutes, hours=hours, days=days)
        await member.timeout(duration, reason=reason)
        await member.send(f"You have been muted for {duration}. \nWith the reason: {reason} ")
        await interaction.response.send_message(f'{member.mention} was timeouted until for {duration}', ephemeral=True)
