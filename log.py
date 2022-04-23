from discord.ext import commands
import logging

class Logger(commands.Cog):

	def __init__(self, bot, config) -> None:
		super().__init__()
		self.bot = bot
		self.setupLog(config)


	def setupLog(self, config):
		log_format = str(config['log_format'])
		log_date = str(config['log_date'])
		historique_log = str(config['historique_log'])

		logging.basicConfig(filename=historique_log,format=log_format, level=logging.INFO)

	def debugLog(msg):
		logging.debug(msg)


	def infoLog(msg):
		logging.info(msg)


	def warningLog(msg):
		logging.warning(msg)


	def errorLog(msg):
		logging.error(msg)


	def criticalLog(msg):
		logging.critical(msg)