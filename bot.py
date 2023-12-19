from aiogram import Bot, Dispatcher, types
from aiogram import executor
import sys
import re
import math

bot = Bot(token="your_token")
dp = Dispatcher(bot)

greet = "Hello! I am a calculator! Just type your expression and I will solve it for you"
gif = "https://media2.giphy.com/media/l2JdZ6jQkHjwlCDkI/giphy.gif?cid=ecf05e47ople536i8wgyl25cvf24e843ir9p6c9boci5jdso&ep=v1_gifs_search&rid=giphy.gif&ct=g"


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton('help'))
    keyboard.add(types.KeyboardButton('solve expression'))
    await message.answer(greet, reply_markup=keyboard)
    await message.answer_animation(gif)


@dp.message_handler(lambda message: message.text in ["help", "/help"])
async def help_handler(message: types.Message):
    await message.reply('Sure! Here are some commands you can use:\n'
                        '/start - Start the bot\n'
                        '/help - Display this help message\n'
                        'Type a mathematical expression to get it solved!\n'
                        'You can also find trigonometric functions (sin, cos, tan). Write them like this: sin(30.0)')


@dp.message_handler(lambda message: message.text == "solve expression")
async def solve_expression_handler(message: types.Message):
    await message.reply('Please type the expression you want to solve')


@dp.message_handler(lambda message: message.text != "")
async def calculate(message: types.Message):
    try:
        expression = message.text
        expression = expression.replace("^", "**")
        expression = expression.replace(":", "/")
        expression = re.sub(r'sin\s*\((.*?)\)', r'math.sin(math.radians(\1))', expression)
        expression = re.sub(r'cos\s*\((.*?)\)', r'math.cos(math.radians(\1))', expression)
        expression = re.sub(r'tan\s*\((.*?)\)', r'math.tan(math.radians(\1))', expression)
        expression = re.sub(r'log\s*\((.*?)\)', r'math.log(\1)', expression)
        numbers = list(map(float, re.findall(r'\b\d+\b', expression)))
        if len(numbers) in [0, 1]:
            await message.answer('Incorrect input. Try again')
        elif any(num > sys.maxsize or num < -sys.maxsize - 1 for num in numbers):
            await message.answer(f'The bot cannot handle such numbers. Try again')
        else:
            result = eval(expression)
            await message.answer(f'{result}')
    except Exception as e:
        await message.answer('An error occurred. Try again')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
