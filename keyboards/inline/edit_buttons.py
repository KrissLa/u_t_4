from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_datas import edit_callback

edit_markup = InlineKeyboardMarkup(row_width=2,
                                   inline_keyboard=[
                                       [
                                           InlineKeyboardButton(
                                               text='Edit Name',
                                               callback_data=edit_callback.new(params_name='name')
                                           ),
                                           InlineKeyboardButton(
                                               text='Edit Description',
                                               callback_data=edit_callback.new(params_name='description')
                                           )
                                       ],
                                       [
                                           InlineKeyboardButton(
                                               text='Edit About',
                                               callback_data=edit_callback.new(params_name='about')
                                           ),
                                           InlineKeyboardButton(
                                               text='Edit Botpic',
                                               callback_data=edit_callback.new(params_name='botpic')
                                           )
                                       ],
                                       [
                                           InlineKeyboardButton(
                                               text='Edit Commands',
                                               callback_data=edit_callback.new(params_name='commands')
                                           ),
                                           InlineKeyboardButton(
                                               text='<< Back to Bot',
                                               callback_data='back_to_bot'
                                           )
                                       ]
                                   ])