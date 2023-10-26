from instagrapi import Client
from logging import Logger


class Instagram:
    def __init__(self, data_json: dict, logger: Logger) -> None:
        self.logger = logger
        username = data_json["meta"]["instagram"]["username"]
        pw = data_json["meta"]["instagram"]["password"]
        self.IG_App = Client()
        self.IG_App.login(username=username, password=pw)
        self.logger.info(f"{username} logged")

    def post_image(
        self,
        caption: str,
        image_path: str,
    ):
        res = self.IG_App.photo_upload(image_path, caption)
        self.logger.info("photo successfully posted")
        return res
