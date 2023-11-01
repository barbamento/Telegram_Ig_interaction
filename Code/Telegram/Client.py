# general import
from logging import Logger
from typing import Callable
import json
import time

# pyrogram
from pyrogram import Client
from pyrogram.types import Message
from pyrogram.handlers.message_handler import MessageHandler


class PyroUser:
    def __init__(self, username, task: dict[str, dict | str], logger: Logger) -> None:
        self.logger = logger
        self.api_id = task["telegram"]["pyro"]["api_id"]
        self.api_hash = task["telegram"]["pyro"]["api_hash"]
        self.logger.info([self.api_id, self.api_hash])
        self.app = Client("username", api_id=self.api_id, api_hash=self.api_hash)

    def start(self):
        self.app.add_handler(MessageHandler(self.send_message_to_bot))
        self.app.run()

    async def send_message_to_bot(self, message: Message):
        message: dict = json.loads(str(message))
        if message["_"] == "Message":
            if str(message["chat"]["id"]) == ["-1001909202660"]:
                if "forward_from_chat" in message.keys():
                    if str(message["forward_from_chat"]) == "-1002096140849":
                        # await self.app.forward_messages(
                        #    "NotizieIABot",
                        #    "-1002096140849",
                        #    message["forward_from_message_id"],
                        # )
                        comand = await self.app.send_message(
                            "-1001909202660", "/post", reply_to_message_id=message["id"]
                        )
                        time.sleep(30)
                        await self.app.delete_messages(
                            "-1001909202660", json.loads(str(comand))["id"]
                        )
