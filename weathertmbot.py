import pyowm
import telebot

owm = pyowm.OWM('6d00d1d4e704068d70191bad2673e0cc',  language='ru')
bot = telebot.TeleBot("737731646:AAEpmJdGRaF9l5GakVnq57Yw1lWrNUKstVc")

@bot.message_handler(content_types = ["text"])
def weather (message):
    observation = owm.weather_at_place(message.text)
    w = observation.get_weather()
    temperature = w.get_temperature('celsius')["temp"]

    answer ="В городе " + message.text + " сейчас " + w.get_detailed_status() +  "\n"
    answer += "Температура равна " + str(temperature) + " градусов по Цельсию\n"

    if temperature >= 25:
        answer += "На улице жарко, можешь идти в футболке"
    elif temperature >= 10:
        answer += "На улице может быть прохладно, одень что-нибудь"
    elif temperature >= 0:
        answer += "На улице весьма холодно, одень куртку"
    elif temperature <= 0:
        answer += "На улице холодина, надень шапку"

    bot.send_message(message.chat.id, answer)

bot.polling(none_stop = True)