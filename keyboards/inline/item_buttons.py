import emoji
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_datas import item_callback


item_markup = InlineKeyboardMarkup(row_width=2,
                                   inline_keyboard=[
                                       [
                                           InlineKeyboardButton(
                                               text="Купить товар",
                                               callback_data=item_callback.new(item_id='1', change_rating='0')
                                           )
                                       ],
                                       [
                                           InlineKeyboardButton(
                                               text=emoji.emojize(f':thumbsup:', use_aliases=True),
                                               callback_data=item_callback.new(item_id='1', change_rating='1')
                                           ),
                                           InlineKeyboardButton(
                                               text=emoji.emojize(f':-1:', use_aliases=True),
                                               callback_data=item_callback.new(item_id='1', change_rating='-1')
                                           )
                                       ],
                                       [
                                           InlineKeyboardButton(
                                               text='Поделиться с другом',
                                               switch_inline_query='1'

                                           )
                                       ]
                                   ])
