from instagrapi import Client
from logging import Logger


class Instagram:
    def __init__(self, data_json: dict, logger: Logger) -> None:
        self.logger = logger
        self.username = data_json["meta"]["instagram"]["username"]
        self.pw = data_json["meta"]["instagram"]["password"]
        self.IG_App = Client()
        self.IG_App.login(username=self.username, password=self.pw)
        self.logger.info(f"{self.username} logged")

    def post_image(
        self,
        caption: str,
        image_path: list[str],
    ):
        try:
            if len(image_path) == 1:
                res = self.IG_App.photo_upload(image_path[0], caption)
                self.logger.info("photo successfully posted")
            else:
                res = self.IG_App.album_upload(image_path, caption)
                self.logger.info("photo successfully posted")
            return res
        except Exception as e:
            self.logger.warning("Could not post  photo. Relogging")
            self.IG_App = Client()
            self.IG_App.login(username=self.username, password=self.pw)
            if len(image_path) == 1:
                res = self.IG_App.photo_upload(image_path[0], caption)
                self.logger.info("photo successfully posted")
            else:
                res = self.IG_App.album_upload(image_path, caption)
                self.logger.info("photo successfully posted")
            return res
