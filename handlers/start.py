from aiogram import types


async def first_msg(message: types.Message):
    await message.answer('все работает')