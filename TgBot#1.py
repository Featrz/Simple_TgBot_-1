import telebot
import time
bot = telebot.TeleBot('')
@bot.message_handler(commands=['start'])
def sendWelcome(message):
    bot.reply_to(message, 'Что-то хотели? /help  /rules')
    timing = time.time()
    while True:
        if time.time() - timing > 6.0*60*60:
            timing = time.time()
            bot.send_message(message.chat.id,
                             "Это чат нашего веб-магазина"
                             "\n Посетить наши ресурсы --> <a href=\"https://info-k.ru\"> Подготовка к ЕГЭ</a>.\n"
                             # "Ознакомься пожалуйста с <a href=\"https://t.me/it_na_divane/3853\"> Правилами </a>"
                             "\n Также вы можете посетить наш курс --> <a href=\"https://xproit.ru\"> PythonProgramming </a>"
                             "\n"
                             "\n Если вы хотите ознакомиться с правилами чата и не получить блокировку, то - /rules"
                             , parse_mode='html', disable_web_page_preview=1)
@bot.message_handler(commands=['rules'])
def sendRules(message):
    bot.send_message(message.chat.id, "<⎯⎯⎯⎯⎯⎯⎯⎯Правила нашего чата⎯⎯⎯⎯⎯⎯⎯⎯>\n"
                     "\n 1. Маты в данном чате запрещены \n"
                     "\n 2. Оскорбления в данном чате запрещены \n"
                     "\n 3. Спам в данном чате запрещен \n")
@bot.message_handler(commands=['help'])
def sendHelp(message):
    bot.send_message(message.chat.id, "Данный чат предназначен для отзывов и обратной связи с клиентами \n"
                     "<a href = \"https://xproit.ru\">PythonProgramming</a>", parse_mode='html', disable_web_page_preview=1)
@bot.message_handler(content_types=['new_chat_members'])
def get_text(message):
    count = bot.get_chat_members_count(message.chat.id)
    if count == 10:
        bot.send_message(message.chat.id, "Our membership equals 10, let's go forward!")
    elif count == 99:
        bot.send_message(message.chat.id, "Almost 100 subs, 1 person is needed to achieve this goal!")
    for user in message.new_chat_members:
        bot.send_message(message.chat.id, "&#128075 Welcome, <a href=\"tg://user?id={0}\">. {1} </a> We are happy to see a new member!\n\n"
                                        "It's our store chat "
                                         "\n U can checkout our website --> <a href=\"https://info-k.ru\"> Prepare for the EGE</a>.\n"
                                         #"Ознакомься пожалуйста с <a href=\"https://t.me/it_na_divane/3853\"> Правилами </a>"
                                          "\nAlso u can check our web Courses here --> <a href=\"https://xproit.ru\"> PythonCourse </a>"
                                          "\n"
                                        "\n If you want, you can checkout a few examples by using command - /start"
                        .format(user.id, user.first_name), parse_mode='html', disable_web_page_preview=1)
# 
GROUP_ID = bot.get_chat('')
banlist = ['бля','сука','даун','даунич','пидор','пидорас','пидорок','гандон','пидорок','хуй','хуек','хуёк','хуесос','еблан','ебать','пиздец','пизда','ебанат']
@bot.message_handler(content_types=['text'])
def handle_text(message):
    print(message.text)
    for i in banlist:
        j = ''
        for o in message.text.lower():
            if o == ' ' or o in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
                j += o
        if i in j.split():
            bot.delete_message(message.chat.id, message.message_id)
            bot.send_message(message.chat.id, 'Маты запрещены в данном чате')
bot.polling(none_stop=True)
