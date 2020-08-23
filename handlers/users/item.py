import logging
import re
from aiogram import types
from aiogram.types import CallbackQuery

from keyboards.inline.callback_datas import item_callback
from keyboards.inline.item_buttons import item_markup
from loader import dp, bot


def get_likes(id):
    item_likes = int(open(f'item_likes_{id}.txt', 'r').read())
    return item_likes

def get_dislikes(id):
    item_dislikes = int(open(f'item_dislikes_{id}.txt', 'r').read())
    return item_dislikes

def add_like(id):
    item_likes = int(open(f'item_likes_{id}.txt', 'r').read())
    item_likes += 1
    il_file = open(f'item_likes_{id}.txt', 'w')
    il_file.write(str(item_likes))
    il_file.close()

def add_dislike(id):
    item_dislikes = int(open(f'item_dislikes_{id}.txt', 'r').read())
    item_dislikes += 1
    id_file = open(f'item_dislikes_{id}.txt', 'w')
    id_file.write(str(item_dislikes))
    id_file.close()

def get_raiting(id):
    item_likes = int(open(f'item_likes_{id}.txt', 'r').read())
    item_dislikes = int(open(f'item_dislikes_{id}.txt', 'r').read())
    rating = item_likes - item_dislikes
    return rating


@dp.message_handler(commands=['item'])
async def get_item(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id,
                         photo='https://lh3.googleusercontent.com/proxy/hwvD8aFR4RyeKyD2rV6brA0kmU5CvJlkY08fqGMzfoYKdCAeri2igMBxC-QSOJlHHforlekTcqMSQhFaqlNF39DliJewjkM7JDHlr6Uz',
                         caption='Мандарины',
                         reply_markup=item_markup)


@dp.callback_query_handler(item_callback.filter(change_rating='0'))
async def show_item(call: CallbackQuery, callback_data: dict):
    await call.answer()
    item_id = callback_data.get('item_id')
    await bot.send_photo(chat_id=call.from_user.id,
                         photo='https://lh3.googleusercontent.com/proxy/hwvD8aFR4RyeKyD2rV6brA0kmU5CvJlkY08fqGMzfoYKdCAeri2igMBxC-QSOJlHHforlekTcqMSQhFaqlNF39DliJewjkM7JDHlr6Uz',
                         caption=f'Покупай товар номер {item_id}')




@dp.callback_query_handler(item_callback.filter(change_rating='1'))
async def like_item(call: CallbackQuery, callback_data: dict):
    item_id = callback_data.get('item_id')
    add_like(item_id)
    item_likes = get_likes(item_id)

    item_dislikes = get_dislikes(item_id)
    rating = get_raiting(item_id)
    await call.answer(
        f"Тебе понравился этот товар. Количество лайков = {item_likes}. Количество дизлайков = {item_dislikes}. Рейтинг = {rating}")


@dp.callback_query_handler(item_callback.filter(change_rating='-1'))
async def dislike_item(call: CallbackQuery, callback_data: dict):
    item_id = callback_data.get('item_id')
    add_dislike(item_id)
    item_dislikes = get_dislikes(item_id)
    item_likes = get_likes(item_id)

    rating = get_raiting(item_id)
    await call.answer(
        f"Тебе не понравился этот товар. Количество лайков = {item_likes}. Количество дизлайков = {item_dislikes}. Рейтинг = {rating}")

