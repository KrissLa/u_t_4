import logging

import emoji
from aiogram import types
from aiogram.types import CallbackQuery

from keyboards.inline.callback_datas import edit_callback
from keyboards.inline.edit_buttons import edit_markup
from loader import dp, bot


@dp.message_handler(commands=['edit'])
async def bot_start(message: types.Message):
    bot_info = await bot.get_me()
    print(bot_info)
    await message.answer(f'Edit {bot_info["username"]} info\n'
                         f'<b>Name:</b> {bot_info["first_name"]}\n'
                         f"{emoji.emojize('<b>Description:</b> :no_entry:')} \n"
                         f"{emoji.emojize('<b>About</b>: :no_entry:')} \n"
                         f"{emoji.emojize('<b>Botpic</b>: :no_entry:')} \n"
                         '<b>Commands:</b> no commands set',
                         reply_markup=edit_markup)


@dp.callback_query_handler(edit_callback.filter(params_name='name'))
@dp.callback_query_handler(edit_callback.filter(params_name='description'))
@dp.callback_query_handler(edit_callback.filter(params_name='about'))
@dp.callback_query_handler(edit_callback.filter(params_name='botpic'))
@dp.callback_query_handler(edit_callback.filter(params_name='commands'))
async def edit_name(call: CallbackQuery, callback_data: dict):
    logging.info(f'callback_data = {call.data}')
    logging.info(f'callback_data dict = {callback_data}')
    params_name = callback_data.get('params_name')
    await call.message.answer(f'Вы нажали на инлайн кнопку, которая отвечает за изменение параметра <b>{params_name}</b>')


@dp.callback_query_handler(text='back_to_bot')
async def edit_name(call: CallbackQuery):
    await call.answer(f"Вы нажали {call.data}")
    await call.message.answer(f"Вы нажали {call.data}")

