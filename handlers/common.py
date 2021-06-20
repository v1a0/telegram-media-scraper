import os
import shutil

from aiogram.types import Message

from settings import CAPTION, HIDE_SOURCE


def file_dir(filename: str, path: str, expansion: str) -> str:
    return f"{path}/{filename}.{expansion}"


def caption_gen(msg: Message) -> str:
    if HIDE_SOURCE:
        return CAPTION
    elif msg.forward_from_chat:
        return CAPTION + f"\n\nsource: {msg.forward_from_chat['title']}"
    else:
        return CAPTION


def remove_temp_files():
    folder = 'saved_files'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)

        except Exception as e:
            pass

