from telegram import Update, Message, File
from telegram.constants import MessageEntityType
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
)
from logging import Logger
from typing import Callable
from pathlib import Path


class Bot:
    def __init__(
        self, task: dict, logger: Logger, on_good_posts: Callable = print
    ) -> None:
        self.logger = logger
        self.on_good_posts = on_good_posts
        self.task = task
        self.page_id = task["telegram"]["id"]
        self.token = task["telegram"]["TOKEN"]
        if not str(self.page_id).startswith("-100"):
            full_id = "-100" + self.page_id
        elif not str(self.page_id).startswith("-") and str(self.page_id).startswith(
            "100"
        ):
            full_id = "-" + self.page_id
        else:
            full_id = self.page_id
        self.full_id = full_id
        self.app = ApplicationBuilder().token(self.token).build()

    def start(self):
        self.app.add_handler(
            CommandHandler(
                ["post"],
                self.parse_post,
            )
        )
        self.logger.info(f"starting telegram bot for page id : {self.full_id}")
        self.app.run_polling(allowed_updates=Update.ALL_TYPES)

    async def parse_post(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        self.logger.info(f"update : {update}")
        if str(update.message.chat_id) == self.full_id:
            if str(update.message.from_user.id) in self.task["telegram"]["admins"]:
                if not update.message.reply_to_message:
                    self.logger.warning("No post selected")
                    await context.bot.send_message(
                        update.message.chat.id,
                        text="No post selected,try again",
                        reply_to_message_id=update.message.id,
                    )
                else:
                    entities = {
                        "caption": update.message.reply_to_message.caption,
                    }
                    if update.message.reply_to_message.caption_entities:
                        for entity in update.message.reply_to_message.caption_entities:
                            if entity.type == MessageEntityType.TEXT_LINK:
                                entities["url"] = entity.url
                    if update.message.reply_to_message.photo:
                        photos = {}
                        for photo in update.message.reply_to_message.photo:
                            photos[photo.file_size] = photo
                        Path(f"data/{self.page_id}").mkdir(parents=True, exist_ok=True)
                        path = f"data/{self.page_id}/{photo.file_unique_id}.jpg"
                        file = await context.bot.get_file(photos[max(photos)])
                        await file.download_to_drive(path)
                        entities["path"] = path
                        self.on_good_posts(entities)
                        return True, entities
                    else:
                        self.logger.warning("No image in selected post")
                        await context.bot.send_message(
                            update.message.chat.id,
                            text="No image in selected post,try again",
                            reply_to_message_id=update.message.id,
                        )
                        return False, {}
        else:
            self.logger.info(f"chat {update.message.chat} not intresting")
        return False, {}


async def parse_NotizieIA_post(
    app: Bot, update: Update, context: ContextTypes.DEFAULT_TYPE
):
    app.logger.info(f"update : {update}")
    if str(update.message.chat_id) == app.full_id:
        if str(update.message.from_user.id) in app.task["telegram"]["admins"]:
            if not update.message.reply_to_message:
                app.logger.warning("No post selected")
                await context.bot.send_message(
                    update.message.chat.id,
                    text="No post selected,try again",
                    reply_to_message_id=update.message.id,
                )
            else:
                entities = {
                    "caption": update.message.reply_to_message.caption,
                }
                if update.message.reply_to_message.caption_entities:
                    for entity in update.message.reply_to_message.caption_entities:
                        if entity.type == MessageEntityType.TEXT_LINK:
                            entities["url"] = entity.url
                if update.message.reply_to_message.photo:
                    photos = {}
                    for photo in update.message.reply_to_message.photo:
                        photos[photo.file_size] = photo
                    Path(f"data/{app.page_id}").mkdir(parents=True, exist_ok=True)
                    path = f"data/{app.page_id}/{photo.file_unique_id}.jpg"
                    file = await context.bot.get_file(photos[max(photos)])
                    await file.download_to_drive(path)
                    entities["path"] = path
                    return True, entities
                else:
                    app.logger.warning("No image in selected post")
                    await context.bot.send_message(
                        update.message.chat.id,
                        text="No image in selected post,try again",
                        reply_to_message_id=update.message.id,
                    )
                    return False, {}
    else:
        app.logger.info(f"chat {update.message.chat} not intresting")
    return False, {}
