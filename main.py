# antontagiev@Antons-MacBook-Air ~ % pip3 install pyTelegramBotAPI==4.4.0

import telebot

bot = telebot.TeleBot('5184273030:AAGtjr2X6ZuOd56hzbgiOtISEYpVGQIJpzw')


@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text == "привет":
        bot.send_message(message.from_user.id, 'здравствуйте!')
    if message.text == "здравствуйте":
        bot.send_message(message.from_user.id, 'здравствуйте!')
    if message.text == "пока":
        bot.send_message(message.from_user.id, 'всего хорошего!')
    if message.text == "давай до свидания":
        bot.send_message(message.from_user.id, 'всего хорошего!')


if __name__ == '__main__':
    bot.polling(none_stop=True)
