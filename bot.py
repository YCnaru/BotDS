import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Ha iniciado sesión como {bot.user}')
    # Comandos disponibles
    commands_list = '''
    *Comandos disponibles:*
    !hello - El bot lo va a saludar 
    !heh - El bot se va a reir
    '''
    channel = bot.get_channel(1369852273814933558)
    await channel.send(commands_list)

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

bot.run("TOKEN")
