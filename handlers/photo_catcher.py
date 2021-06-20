from misc import dp
from classes import Branch
from aiogram.dispatcher import FSMContext
from aiogram.types.photo_size import PhotoSize
from aiogram.types import InputFile, ContentTypes, Message
from settings import CHANNELS, PM
from messages import MESSAGES as MSGS
from handlers.common import file_dir, caption_gen, remove_temp_files


def pic_dir(name: str) -> str:
    return file_dir(filename=name, path='saved_files', expansion='jpg')


async def pic_prep(pic: PhotoSize) -> InputFile:
    pic_path = pic_dir(name=pic.file_unique_id)
    await pic.download(pic_path)
    return InputFile(pic_path)


@dp.message_handler(state=Branch.default, content_types=ContentTypes.PHOTO)
async def start(message: Message, state: FSMContext):
    for ch_id in CHANNELS:
        await dp.bot.send_photo(
            chat_id=ch_id, caption=caption_gen(message), parse_mode=PM,
            photo=await pic_prep(message.photo[-1])
        )

    remove_temp_files()
    await message.reply(MSGS['forwarded'])
