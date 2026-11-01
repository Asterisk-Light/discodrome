'''An extention containing functionality exclusive to the bot owner'''

import logging
from discord import app_commands, Interaction
from discord.ext import commands
from discodrome import DiscodromeClient
from util import env

logger = logging.getLogger(__name__)

class OwnerCog(commands.Cog):
    ''' A Cog containing owner specific commands '''
    
    bot: DiscodromeClient
    
    def __init__(self, bot: DiscodromeClient):
        self.bot = bot
    
    @commands.hybrid_command(name="sync", description="Sync slash commands")
    @commands.check(lambda ctx: ctx.author.id == env.DISCORD_OWNER_ID)
    @app_commands.check(lambda interaction: interaction.user.id == env.DISCORD_OWNER_ID)
    async def sync(self, ctx: commands.Context):
        await self.bot.sync_command_tree()
        await ctx.send("Commands synced")

async def setup(bot: DiscodromeClient):
    ''' Setup function for the owner.py cog '''

    await bot.add_cog(OwnerCog(bot))
