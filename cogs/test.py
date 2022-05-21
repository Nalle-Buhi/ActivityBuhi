import discord
from discord import app_commands
from discord.ext import commands
import botconfig
from tools.embedtools import embedtool

class MyCog(commands.Cog):
  def __init__(self, bot: commands.Bot):
    self.bot = bot

    @commands.Cog.listener()
    async def on_message(msg):
        print("Message")


  @app_commands.command(name="embedtest")
  async def embedtest(self, interaction):
    embed = await embedtool(interaction, "kives", "kives2")
    await interaction.response.send_message("Mutsis on", ephemeral=False, embed=embed)


async def setup(bot: commands.Bot):
  await bot.add_cog(MyCog(bot), guilds=[discord.Object(id=botconfig.TEST_GUILD)])
