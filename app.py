from aiogram import types, Bot, Dispatcher
import asyncio
from aiogram.filters import Filter  
from aiogram.filters.chat_member_updated import IS_NOT_MEMBER, IS_MEMBER, ChatMemberUpdatedFilter
from aiogram.types import ChatMemberUpdated  

token = '8086638679:AAFCar2Dobp-A3aulaBQA8mudgK9-6uOq6g'
bot = Bot(token)
dp = Dispatcher()

class Myfilter(Filter):
    async def __call__(self, message: types.Message):
        return message.chat.type in ['group', 'supergroup']
    
@dp.message(Myfilter())
async def get_message(event: types.Message):
    print(event.json())
    await event.delete()


class Myfilter1(Filter):
    async def __call__(self, message: types.Message):
        return message.chat.type in ['private']
    


@dp.message(lambda message: message.text, Myfilter1())
async def get_message(msg: types.Message):
    await msg.answer(text="Assalamu Aleykum Cleaner data botga xush kelibsiz")


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())