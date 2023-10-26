import json

from Code.Utils.Logger import create_logger
from Code.Bot import Bot
from Code.Telegram.Bot import Bot as TG_Bot


if __name__ == "__main__":
    page = "NotizieIA"
    with open(f"secrets/{page}.json", "r") as f:
        notizieIA = json.loads(f.read())
    logger = create_logger(page)
    b = Bot(
        notizieIA,
        ["fb", "insta"],
        logger,
    )
    tg = TG_Bot(notizieIA, logger, b.post_photo)
    tg.start()
