from typing import List
from logging import Logger
from Code.Meta.App import App
from Code.Meta.Facebook import Facebook
from Code.Meta.Instagram import Instagram


class Bot:
    def __init__(self, task: dict, socials: List[str], logger: Logger) -> None:
        self.logger = logger
        apps = {}
        for s in socials:
            if s.lower() in ["ig", "insta", "instagram"]:
                apps["instagram"] = Instagram(task, logger)
                self.logger.info("Ig added to app")
            elif s.lower() in ["fb", "face", "facebook"]:
                app = App(task, logger)
                apps["facebook"] = Facebook(app)
                self.logger.info("Fb added to app")
            else:
                raise AssertionError(f"{s} is not supported Yet")
        self.apps = apps
        self.task = task

    def post_photo(self, entities):
        caption = entities["caption"] + "\n" + entities["url"]
        image_path = entities["path"]
        for app in self.apps.values():
            if isinstance(app, Instagram):
                app.post_image(caption, image_path)
            elif isinstance(app, Facebook):
                app.post_image(caption, image_path)
        self.logger.info("image posted on all apps")
