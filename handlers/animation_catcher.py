from misc import dp
from classes import Branch
from aiogram.dispatcher import FSMContext
from aiogram.types.animation import Animation
from aiogram.types import ContentTypes, Message
from settings import CHANNELS, PM
from messages import MESSAGES as MSGS
from handlers.common import file_dir, caption_gen, remove_temp_files


def animation_dir(name: str) -> str:
    return file_dir(filename=name, path='saved_files', expansion='mp4')


async def animation_prep(anim: Animation) -> bin:
    anim_path = animation_dir(name=anim.file_unique_id)
    await anim.download(anim_path)
    return open(anim_path, 'rb')


@dp.message_handler(state=Branch.default, content_types=ContentTypes.ANIMATION)
async def start(message: Message, state: FSMContext):
    for ch_id in CHANNELS:
        await dp.bot.send_animation(
            chat_id=ch_id, caption=caption_gen(message), parse_mode=PM,
            animation=await animation_prep(message.animation),
        )
    remove_temp_files()
    await message.reply(MSGS['forwarded'])

