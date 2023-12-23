import asyncio
from aiogram import Bot, Dispatcher

from handlers import user_commands

BOT_TOKEN = '6630213255:AAFLwGCUgqVeqTQFATq-eSZU7fPWzNYDwTQ'


async def main():
    bot = Bot(BOT_TOKEN, parse_mode='HTML')
    dp = Dispatcher()


    dp.include_routers(
        user_commands.router,
    )

    # main_menu_commands = [
    #     BotCommand(command='/start', description='Начать работу'),
    #     BotCommand(command='/help', description='Получить справочную информацию'),
    #     BotCommand(command='/projects', description='Список проектов'),
    #     BotCommand(command='/fill_resume', description='Заполнить или обновить резюме')
    # ]

    # await bot.set_my_commands(main_menu_commands)

    await bot.delete_webhook(drop_pending_updates=True)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(main())
