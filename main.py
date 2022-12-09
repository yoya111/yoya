from aiogram import types, executor, Dispatcher, Bot
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

t = "5817337878:AAG5qEjJ6AKbw4_-imUN4fW0ew9zwWWe5ec"
bot = Bot(token=t)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.message):
 await bot.send_message(message.chat.id, "Выберите героя, а я рассчитаю вам шансы на выпадение сета! \n Сколько коробок у вас уже открыто?")

p = 14

chance = p
text = "1 к", chance



@dp.message_handler(commands=['Hoodwink'])
async def Hoodwink_command(message: types.Message):
    await bot.send_message(message.from_user.id, text,reply_markup=but_cl)
b1 = KeyboardButton('/Hoodwink')

@dp.message_handler(commands=['Riki'])
async def Riki_command(message: types.Message):
          await bot.send_message(message.from_user.id, text,reply_markup=but_cl)
b2 = KeyboardButton('/Riki')

@dp.message_handler(commands=['Snapfire'])
async def Snapfire_command(message: types.Message):
          await bot.send_message(message.from_user.id, text,reply_markup=but_cl)
b3 = KeyboardButton('/Snapfire')

@dp.message_handler(commands=['Chen'])
async def Chen_command(message: types.Message):
          await bot.send_message(message.from_user.id, text,reply_markup=but_cl)
b4 = KeyboardButton('/Chen')

@dp.message_handler(commands=['Сlockwerk'])
async def Сlockwerk_command(message: types.Message):
          await bot.send_message(message.from_user.id, text,reply_markup=but_cl)
b5 = KeyboardButton('/Сlockwerk')

@dp.message_handler(commands=['Dawnbreaker'])
async def Dawnbreaker_command(message: types.Message):
          await bot.send_message(message.from_user.id, text,reply_markup=but_cl)
b6 = KeyboardButton('/Dawnbreaker')

@dp.message_handler(commands=['Spectre'])
async def Spectre_command(message: types.Message):
          await bot.send_message(message.from_user.id, text,reply_markup=but_cl)
b7 = KeyboardButton('/Spectre')

@dp.message_handler(commands=['Void'])
async def Void_command(message: types.Message):
          await bot.send_message(message.from_user.id, text,reply_markup=but_cl)
b8 = KeyboardButton('/Void')

@dp.message_handler(commands=['Ursa'])
async def Ursa_command(message: types.Message):
          await bot.send_message(message.from_user.id, text,reply_markup=but_cl)
b9 = KeyboardButton('/Ursa')

@dp.message_handler(commands=['Phoenix'])
async def Phoenix_command(message: types.Message):
          await bot.send_message(message.from_user.id, text,reply_markup=but_cl)
b10 = KeyboardButton('/Phoenix')

@dp.message_handler(commands=['Terrorblade'])
async def Terrorblade_command(message: types.Message):
          await bot.send_message(message.from_user.id, text,reply_markup=but_cl)
b11 = KeyboardButton('/Terrorblade')

@dp.message_handler(commands=['Undying'])
async def Undying_command(message: types.Message):
          await bot.send_message(message.from_user.id, text,reply_markup=but_cl)
b12 = KeyboardButton('/Undying')

@dp.message_handler(commands=['Monkey'])
async def Monkey_command(message: types.Message):
          await bot.send_message(message.from_user.id, text,reply_markup=but_cl)
b13 = KeyboardButton ('/Monkey')

@dp.message_handler(commands=['Witch'])
async def Witch_command(message: types.Message):
          await bot.send_message(message.from_user.id, text,reply_markup=but_cl)
b14 = KeyboardButton('/Witch')

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(Hoodwink_command, commands=['/Hoodwink'])
    dp.register_message_handler(Snapfire_command, commands=['/Snapfire'])
    dp.register_message_handler(Chen_command, commands=['/Chen'])
    dp.register_message_handler(Сlockwerk_command, commands=['/Сlockwerk'])
    dp.register_message_handler(Dawnbreaker_command, commands=['/Dawnbreaker'])
    dp.register_message_handler(Spectre_command, commands=['/Spectre'])
    dp.register_message_handler(Void_command, commands=['/Void'])
    dp.register_message_handler(Ursa_command, commands=['/Ursa'])
    dp.register_message_handler(Phoenix_command, commands=['/Phoenix'])
    dp.register_message_handler(Terrorblade_command, commands=['/Terrorblade'])
    dp.register_message_handler(Undying_command, commands=['/Undying'])
    dp.register_message_handler(Monkey_command, commands=['/Monkey'])
    dp.register_message_handler(Witch_command, commands=['/Witch'])
    dp.register_message_handler(Riki_command, commands=['/Riki'])

but_cl = ReplyKeyboardMarkup()

but_cl.add(b1).add(b2).add(b3).add(b4).add(b5).add(b6).add(b7).add(b8).add(b9).add(b10).add(b11).add(b12).add(b13).add(b14)


executor.start_polling(dp)