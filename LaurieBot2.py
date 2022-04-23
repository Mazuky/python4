from click import pass_context
from discord.ext import commands
import discord
from discord.ext.commands import Bot
from discord.ext.commands.context import Context
from log import Logger
from argparse import ArgumentParser, Namespace
import argparse
import json

class LoloBot(Bot):

	def __init__(self, config):
		super().__init__(str(config['prefix']))
		
		self.add_cog(CMD(self))
		self.add_cog(Logger(self, config))


	async def on_ready(self):
		print(f'{self.user} est connecté(e) a Discord!')


def get_args() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument(
        "-c", "--config", help="Config file", required=True, dest="config"
    )
    return parser.parse_args()

def get_config(config_file: str)-> dict:

    with open(config_file, "r") as f:

        config = json.load(f)

    return config




def main():
	args = get_args()
	config = json.load(open(args.config))
	
	bot = LoloBot(config)
	bot.run(str(config['token']))


class CMD(commands.Cog):
	
	def __init__(self, bot) -> None:
		super().__init__()
		self.bot = bot


	@commands.command(name="temps", pass_context=True)
	async def temps(self, ctx):
		msg = f"{ctx.message.author.name} a dit " + str(ctx.message.content)
		Logger.infoLog(msg)
		await ctx.send("Tu es mon soleil :sun_with_face:")

	@commands.command(name="HELP", pass_context=True)
	async def HELP(self, ctx):
		msg = f"{ctx.message.author.name} a dit " + str(ctx.message.content)
		Logger.infoLog(msg)
		await ctx.send("les commandes possibles sont : temps")

if __name__ == "__main__":
	main()