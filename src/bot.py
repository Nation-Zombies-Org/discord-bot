import os
import asyncio
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Basic Settings
TOKEN = os.getenv('DISCORD_BOT_TOKEN')
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

async def main():
    """Main function for loading extensions and starting the bot."""
# Load extensions
    await bot.load_extension('commands.buy')
    await bot.load_extension('commands.vip')
    await bot.load_extension('commands.server_info')

# Initiate the bot
    await bot.start(TOKEN)

@bot.event
async def on_ready():
    print(f"Bot connected as {bot.user}")

# Perform the main function
if __name__ == "__main__":
    asyncio.run(main())