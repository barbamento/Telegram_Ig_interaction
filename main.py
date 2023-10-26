import json

from Code.Utils.Logger import create_logger
from Code.Bot import Bot

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
    b.post_photo(
        # "Centrali nucleari senza autorizzazione, la maggioranza tenta il blitz notturno",
        # image_path="data/prova.jpg"
    )
