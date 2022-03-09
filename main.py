import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import dinner
import trailer

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    for guild in bot.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{bot.user} is connected to the following guild:\n')
    for guilds in bot.guilds:
        print(guilds.name)


@bot.command()
async def middag(ctx):
    food = dinner.whatToEat()
    await ctx.send(food)

@bot.command()
async def trailers(ctx):
    response = trailer.trailer()
    await ctx.send(response)

@bot.command()
async def YT(ctx, message):
    await ctx.send(message)


async def list_servers():
    await bot.wait_until_ready()
    while not bot.is_closed:
        print("Current servers:")
        for server in bot.servers:
            print(server.name)
        await asyncio.sleep(600)


if __name__ == '__main__':
    bot.loop.create_task(list_servers())
    bot.run(TOKEN)