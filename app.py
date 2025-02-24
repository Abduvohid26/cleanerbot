from aiogram import types, Bot, Dispatcher, F
from aiogram.filters import Filter  
from aiogram.filters.chat_member_updated import IS_NOT_MEMBER, IS_MEMBER, ChatMemberUpdatedFilter
from aiogram.types import ChatMemberUpdated  
import logging
import sys
from decouple import config
import asyncio


token = config('BOT_TOKEN')
ADMINS = config('ADMINS').split(" ")


bot = Bot(token)
dp = Dispatcher()

class Myfilter(Filter):
    async def __call__(self, message: types.Message):
        return message.chat.type in ['group', 'supergroup']
    
@dp.message(Myfilter(),  F.new_chat_members)
async def get_message(event: types.Message):
    print(event.json())
    await event.delete()

@dp.message(Myfilter(), F.left_chat_member)
async def get_message(event: types.Message):
    print(event.json())
    await event.delete()


class Myfilter1(Filter):
    async def __call__(self, message: types.Message):
        return message.chat.type in ['private']
    


@dp.message(lambda message: message.text, Myfilter1())
async def get_message(msg: types.Message):
    print(msg.json())
    await msg.answer(text="Assalamu Aleykum Cleaner data botga xush kelibsiz")



async def start():
    for i in ADMINS:
        try:
            await bot.send_message(chat_id=i,text="Bot faollashdi!")
        except:
            pass
async def shutdown():
    for i in ADMINS:
        try:
            await bot.send_message(chat_id=i,text="Bot to'xtadi!")
        except:
            pass


async def main():
    dp.startup.register(start)
    dp.shutdown.register(shutdown)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
                        handlers=[
                            logging.FileHandler('bot.log'),
                            logging.StreamHandler(sys.stdout)
                        ]
                        )
    asyncio.run(main())