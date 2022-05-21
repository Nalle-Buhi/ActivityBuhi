import discord
from discord.ext import commands
import os
import botconfig


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix='buhi ',
            intents = discord.Intents(messages = True, message_content = True, members = True, presences = True),
            application_id = botconfig.APP_ID
        )

    async def setup_hook(self):
        for filename in os.listdir("cogs"):
            if filename.endswith(".py"):
                await self.load_extension(f"cogs.{filename[:-3]}")
                print(f"loaded: {filename}")
        await bot.tree.sync(guild = discord.Object(id=botconfig.TEST_GUILD))

    async def on_ready(self):
        print(f"Logged in as: {bot.user}")



if __name__ == "__main__":
    bot = Bot()
    bot.run(botconfig.TOKEN)
