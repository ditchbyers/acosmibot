import discord
from discord.ext import commands
from discord import app_commands
import logging
import requests
from dotenv import load_dotenv
import os
from datetime import datetime

class Help(commands.Cog):
    def __init__(self, bot:commands.Bot):
        super().__init__()
        self.bot = bot
        load_dotenv()
        self.URL = os.getenv('URL')
        
    @app_commands.command(name = "help", description = "Returns a list of commands.")
    async def help(self, interaction: discord.Interaction):
        embed = discord.Embed(title="Acosmibot - Commands", color=interaction.user.color)
        embed.add_field(name="/rank", value="Returns your current rank based on exp and general stats.", inline=False)
        embed.add_field(name="/balance", value="Returns your current balance.", inline=False)
        embed.add_field(name="/give", value="Give another member some of your Credits.", inline=False)
        embed.add_field(name="/leaderboard", value="Returns top 5 members by your selected stat.", inline=False)
        embed.add_field(name="/coinflip", value="Flip a coin for a chance to win Credits.", inline=False)
        embed.add_field(name="/checkvault", value="Returns the current balance of the vault. Gamba losses go in vault.", inline=False)
        embed.add_field(name="/rockpaperscissors", value="Challenge another member to a game of Rock, Paper, Scissors. Win 3 rounds!", inline=False)
        embed.add_field(name="/8ball", value="Ask the magic 8ball your yes/no questions for 10 Credits.", inline=False)
        embed.add_field(name="/polymorph", value="Change your target's display name for 1000 Credits.", inline=False)
        embed.add_field(name="/weather", value="Returns the current weather in a city.", inline=False)
        embed.add_field(name="/apod", value="Returns the Astronomy Picture of the Day.", inline=False)
        embed.add_field(name="/help", value="Returns a list of commands.", inline=False)
        embed.add_field(name="", value="[Developed by Acosmic](https://github.com/acosmic/acosmicord-bot) <a:pepesith:1165101386921418792>", inline=False)

        # embed.set_footer(text="Developed by Acosmic")
        await interaction.response.send_message(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(Help(bot))