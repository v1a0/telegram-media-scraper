from aiogram.dispatcher.filters.state import State, StatesGroup


class Branch(StatesGroup):
    banned = State()
    default = State()
    settings = State()
