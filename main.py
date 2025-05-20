import disnake
from disnake.ext import commands
from config import SOURCE_GUILD_ID, TARGET_GUILD_ID, TOKEN
from utils.channels import clone_channels
from utils.roles import clone_roles

intents = disnake.Intents.all()
bot = commands.Bot(command_prefix="!!", intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

    source = bot.get_guild(SOURCE_GUILD_ID)
    target = bot.get_guild(TARGET_GUILD_ID)

    if not source or not target:
        print("Source or target guild not found.")
        await bot.close()

    print(f"Source guild: {source.name}\nTarget guild: {target.name}")

    print("Starting copy...")
    await clone_roles(source, target)
    await clone_channels(source, target)
    print("Copying done")

    await bot.close()


bot.run(TOKEN)
