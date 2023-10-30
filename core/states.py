from aiogram.fsm.state import State, StatesGroup


class AggregateBotState(StatesGroup):
    main_menu = State()
