import logging

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from . import text_messages as texts
from .states import AggregateBotState
from common import services, database

router = Router()

logger = logging.getLogger(__name__)


@router.message(Command("start"))
async def start_command_function(message: Message, state: FSMContext):
    user_nickname = message.from_user.full_name
    await message.answer(text=texts.HELLO_TEXT.format(user_nickname=user_nickname))
    await state.set_state(AggregateBotState.main_menu)


@router.message(Command("help"))
async def help_command_function(message: Message, state: FSMContext):
    await message.answer(text=texts.HELP_TEXT)
    await state.set_state(AggregateBotState.main_menu)


@router.message(F.text)
async def user_input(message: Message, state: FSMContext):
    data = message.text
    json_format = await services.has_json_format(data)
    correct_length = await services.has_correct_length(data)
    items_valid = await services.are_items_valid(data)
    dates_valid = await services.are_dates_valid(data)

    if json_format and correct_length and items_valid and dates_valid:
        dict_data = await services.get_dict_data(data)
        if dict_data["group_type"] == "month":
            output_data = await database.get_month_collection(
                dict_data["dt_from"], dict_data["dt_upto"]
            )
        elif dict_data["group_type"] == "day":
            output_data = await database.get_day_collection(
                dict_data["dt_from"], dict_data["dt_upto"]
            )
        elif dict_data["group_type"] == "hour":
            output_data = await database.get_hour_collection(
                dict_data["dt_from"], dict_data["dt_upto"]
            )
        await message.answer(text=str(output_data))
    else:
        await message.answer(text=texts.ERROR_MESSAGE_TEXT)

    await state.set_state(AggregateBotState.main_menu)
