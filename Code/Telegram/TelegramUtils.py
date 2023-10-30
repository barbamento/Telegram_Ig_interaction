from telegram import Message, PhotoSize


def extract_photos(message: Message) -> dict[str, PhotoSize]:
    photos = {}
    for photo in message.reply_to_message.photo:
        photos[photo.file_size] = photo
    return photos
