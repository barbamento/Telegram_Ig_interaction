from .App import App


class Facebook:
    def __init__(self, app: App) -> None:
        self.logger = app.logger
        self.raw_app = app
        self.fb_app = app.app_API

    def post_text(self, caption: str, image_path) -> dict:
        res = self.fb_app.put_object(
            "me", "feed", message=caption, image=open(image_path, "rb")
        )
        return res

    def post_image(self, caption: str, image_path: str) -> dict:
        res = self.fb_app.put_photo(
            image=open(image_path, "rb"),
            message=caption,
            # album_path=self.raw_app.me["id"] + "/picture",
        )
        if "post_id" in res:
            self.logger.info("Image succesfully posted")
        else:
            self.logger.warning(f"An error occurred while posting {image_path}")
        return res
