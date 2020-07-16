from telebot.types import Message

from main import bot


@bot.message_handler(commands=['/go'])
async def start_command(msg: Message) -> None:
    await bot.send_message(msg.chat.id, f'Hello, you wrote me "{msg.text}"')
