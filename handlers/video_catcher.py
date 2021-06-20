from misc import dp
from classes import Branch
from aiogram.dispatcher import FSMContext
from aiogram.types.video import Video
from aiogram.types import ContentTypes, Message
from settings import CHANNELS, PM
from messages import MESSAGES as MSGS
from handlers.common import file_dir, caption_gen, remove_temp_files


def video_dir(name: str) -> str:
    return file_dir(filename=name, path='saved_files', expansion='mp4')


async def video_prep(vid: Video) -> bin:
    video_path = video_dir(name=vid.file_unique_id)
    await vid.download(video_path)
    return open(video_path, 'rb')


@dp.message_handler(state=Branch.default, content_types=ContentTypes.VIDEO)
async def start(message: Message, state: FSMContext):
    for ch_id in CHANNELS:
        await dp.bot.send_video(
            chat_id=ch_id, caption=caption_gen(message), parse_mode=PM,
            video=await video_prep(message.video),
            supports_streaming=True
        )

    remove_temp_files()
    await message.reply(MSGS['forwarded'])

