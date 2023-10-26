import facebook as fb
from logging import Logger
from datetime import datetime


class App:
    def __init__(self, meta_json: dict, logger: Logger) -> None:
        self.logger = logger
        self.app_secret = meta_json["meta"]["app"]["secret"]
        self.app_id = meta_json["meta"]["app"]["app_id"]
        self.page_access_token = meta_json["meta"]["page_access_token"]["value"]
        self.app_API = fb.GraphAPI(self.page_access_token)
        self.extend_pagetoken()
        self.me = self.app_API.get_object("me")
        self.logger.info(f"Logged on : {self.me['name']} , id : {self.me['id']}")

    def extend_pagetoken(self):
        timestamp_now = datetime.now().replace(microsecond=0).timestamp()
        res_debug = self.app_API.debug_access_token(
            self.page_access_token, self.app_id, self.app_secret
        )["data"]
        self.logger.info(
            f"token expires at : {res_debug['expires_at']} , current time is : {timestamp_now}"
        )
        if timestamp_now - res_debug["expires_at"] < 60 * 60 * 24:
            self.logger.info("extending access")
            res = self.app_API.extend_access_token(
                app_id=self.app_id, app_secret=self.app_secret
            )
            self.page_access_token = res["access_token"]
            print(self.page_access_token)
