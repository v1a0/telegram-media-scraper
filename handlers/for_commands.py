from misc import dp
from classes import Branch
from keyboards.keyboards import *
from aiogram import types
from messages import MESSAGES
from settings import ADMIN_ID


@dp.message_handler(state='*', commands=['start', 'stop'])
async def start(message: types.Message):

    if message.from_user.id in ADMIN_ID:
        await Branch.default.set()
        await message.reply(MESSAGES['admin'], reply_markup=default_keyboard())

    else:
        await Branch.banned.set()
#        await message.reply(MESSAGES['banned'], reply_markup=types.ReplyKeyboardRemove())

