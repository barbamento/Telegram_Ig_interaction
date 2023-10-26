from telegram import Update, Message
from telegram.ext import (
    filters,
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
    MessageHandler,
)
from logging import Logger


class Bot:
    def __init__(self, token: str, id: str, logger: Logger) -> None:
        self.logger = logger
        self.app_id = id
        self.app = ApplicationBuilder().token(token).build()

    # def __post_init__(self):

    def start(self):
        self.app.add_handler(MessageHandler(filters.ALL, self.get_correct_post))
        print("starting")
        self.app.run_polling()

    # @staticmethod
    # async def id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    #    await context.bot.send_message("-1001909202660", update.effective_chat.id)

    # @staticmethod
    # async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    #    await context.bot.send_message("barbamento", "ciao")

    async def get_correct_post(
        self, message: Message, context: ContextTypes.DEFAULT_TYPE
    ):
        if message:
            self.logger.info(f"message : {message}")
