import telebot
from random import randint # для казиныча
import time
import db
import datetime


TOKEN = '1710589285:AAGPBaALjUILIyaRh39K-sushILAETlz8G8'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['balance'])
def send_users_stat(message):
	bot.reply_to(message, db.get_users_stat_from_db(), parse_mode='HTML')

@bot.message_handler(commands=['azino777', 'cazino', 'cazino777', 'casino777', 'kazino', 'kasino', 'казино', 'Казино', 'Казино777', 'казино777'])
def send_to_maiorchik(message):
    bot.reply_to(message, 'Необучаемый, блядь')

@bot.message_handler(commands=['update'])
def send_update(message):
	bot.reply_to(message, """07.04.2021. \n Починил, что бот не заводил пользователя в БД при вызове казино \n Быстрофикс минусовых ставок в казино. \n Поправил шансы казно. Мы выигрываем чаще. \n Добавил реакцию на дай рофлан \n  TODO:     Удаление кучи сообщений из козиныча(?) по таймауту
    функция реагирования на сообщения "дай рофл" "дайте рофл" и т.д ДОПИСАТЬ
    вести бомжей в БД
    функция реагирования на событие улетания в минус рофлов пользователя
    рофлокредит
    запилить ранги""")

@bot.message_handler(commands=['github_link'])
def send_update(message):
	bot.reply_to(message, 'https://github.com/yourh3ro/degrot_karma_bot')

@bot.message_handler(regexp="^[+]")
def add_rofl_when_reply(message):
    if message.reply_to_message is not None:
        if message.from_user.username == message.reply_to_message.json['from']['username']:
            bot.reply_to(message, 'Сам себя плюсуешь? Думал наебать меня?')
        balance = db.get_roflanbalance_from_db(str(message.from_user.username))
        if balance < 1:
            bot.reply_to(message, 'Не хватает рофлов! Бери пример, бомжара') 
        else:
            random_rofl = randint(1,50)
            if random_rofl == 1:
                bot.send_message(message.chat.id, 'Еееееебать! МЕГАРОФЛ!')
                bot.send_message(message.chat.id, '@' + message.from_user.username + ' дал МЕГАРОФЛ ' + '@' + message.reply_to_message.json['from']['username'])

                db.db_add_rofl(str(message.from_user.username), str(message.reply_to_message.json['from']['username']), 5)
                db.db_remove_rofl(str(message.reply_to_message.json['from']['username']), str(message.from_user.username), 5)

                bot.send_message(message.chat.id, db.get_one_user_stat_from_db(str(message.reply_to_message.json['from']['username'])), parse_mode='HTML')
            else:
                bot.send_message(message.chat.id, '@' + message.from_user.username + ' дал рофлан ' + '@' + message.reply_to_message.json['from']['username'])

                db.db_add_rofl(str(message.from_user.username), str(message.reply_to_message.json['from']['username']), 1)
                db.db_remove_rofl(str(message.reply_to_message.json['from']['username']), str(message.from_user.username), 1)

                bot.send_message(message.chat.id, db.get_one_user_stat_from_db(str(message.reply_to_message.json['from']['username'])), parse_mode='HTML')

@bot.message_handler(regexp="^[-]")
def remove_rofl_when_reply(message):
    if message.reply_to_message is not None:
        if message.from_user.username == message.reply_to_message.json['from']['username']:
            bot.reply_to(message, 'ХАХА тут долбаеб сам себе минусы ставит')
        else:
            random_rofl = randint(1,50)
            if random_rofl == 1:
                bot.send_message(message.chat.id, 'Еееееебать! МЕГАМИНУС!')
                bot.send_message(message.chat.id, '@' + message.from_user.username + ' залил МЕГАМИНУС ' + '@' + message.reply_to_message.json['from']['username'])

                db.db_remove_rofl(str(message.from_user.username), str(message.reply_to_message.json['from']['username']), 5)
                db.db_add_rofl(str(message.from_user.username), db.casino_admin, 5)

                bot.send_message(message.chat.id, db.get_one_user_stat_from_db(str(message.reply_to_message.json['from']['username'])), parse_mode='HTML')
            elif random_rofl == 2:
                bot.send_message(message.chat.id, 'ГУЧИ ЛИНЗЫ ОТРАЗИЛИ ХЕЙТ')
                bot.send_message(message.chat.id,'@' + message.reply_to_message.json['from']['username'] + ' ОТРАЗИЛ ХЕЙТ ' + '@' + message.from_user.username)

                db.db_remove_rofl(str(message.reply_to_message.json['from']['username']), str(message.from_user.username), 5)
                db.db_add_rofl(str(message.from_user.username), db.casino_admin, 5)

                bot.send_message(message.chat.id, db.get_one_user_stat_from_db(str(message.from_user.username)), parse_mode='HTML')
            else:
                bot.send_message(message.chat.id, '@' + message.from_user.username + ' залил соляры ' + '@' + message.reply_to_message.json['from']['username'])

                db.db_remove_rofl(str(message.from_user.username), str(message.reply_to_message.json['from']['username']), 1)
                db.db_add_rofl(str(message.from_user.username), db.casino_admin, 1)

                bot.send_message(message.chat.id, db.get_one_user_stat_from_db(str(message.reply_to_message.json['from']['username'])), parse_mode='HTML')
    
@bot.message_handler(regexp="дай[\s]рофл")
def bomj(message):
    randfraza = randint(1,3)
    if randfraza == 1:
        bot.reply_to(message, "Бомжара ебаная")
    if randfraza == 2:
        bot.reply_to(message, "А пососать не завернуть?")
    if randfraza == 3:
        bot.reply_to(message, "Еще чего?")

@bot.message_handler(regexp="casino [0-9]*")
def new_casino(message):

    now_time = datetime.datetime.now()
    last_casino_action = db.db_get_casino_time(str(message.from_user.username))
    casino_action_succes_time = last_casino_action + datetime.timedelta(minutes=45)

    rate = int(message.text[7:])
    if rate <= 0:
        bot.send_message(message.chat.id, 'Наебать меня думал?')
    else:
        balance = db.get_roflanbalance_from_db(str(message.from_user.username))
        if balance < rate:
            bot.send_message(message.chat.id, 'На что играть собрался? Не хватает рофлов')
            if casino_action_succes_time > now_time:
                time_to_casino = casino_action_succes_time - now_time
                time_to_casino = str(time_to_casino)
                bot.send_message(message.chat.id, f'РАНО БЛЯТЬ! жди {time_to_casino}')
            else:
                bot.reply_to(message, "Кручу... Верчу... Наебать хочу!")
                time.sleep(2)
                result_of_casino = randint(1,100)
                roflan_count = rate

                array_of_procents_lose = []
                array_of_procents_win = []

                i = 10
                while i <= 40:
                    array_of_procents_lose.append(i)
                    i = i + 1

                q = 41
                while q <= 100:
                    array_of_procents_win.append(q)
                    q = q + 1

                if result_of_casino == 1 or result_of_casino == 2 or result_of_casino == 3 or result_of_casino == 4 or result_of_casino == 5:
                    bot.send_message(message.chat.id, f'Ты проебал все! -{str(balance)} рофлов')
                    bot.send_message(message.chat.id, f'СОСАТЬ! casino_admin +{str(balance)} рофлов')
                    db.db_remove_rofl(db.casino_admin, str(message.from_user.username), balance)
                    db.db_add_rofl(str(message.from_user.username), db.casino_admin, balance)
                    bot.send_message(message.chat.id, db.get_one_user_stat_from_db('casino_admin'), parse_mode='HTML')
                    bot.send_message(message.chat.id, db.get_one_user_stat_from_db(str(message.from_user.username)), parse_mode='HTML')
                if result_of_casino == 6 or result_of_casino == 7 or result_of_casino == 8 or result_of_casino == 9 or result_of_casino == 10:
                    bot.send_message(message.chat.id, f'Ты проебал жизнь! -{str(balance * 2)} рофлов')
                    bot.send_message(message.chat.id, f'Твоя жизнь пренадлежит мне, еблан! casino_admin +{str(balance * 2)} рофлов')
                    db.db_remove_rofl(db.casino_admin, str(message.from_user.username), balance * 2)
                    db.db_add_rofl(str(message.from_user.username), db.casino_admin, balance * 2)
                    bot.send_message(message.chat.id, db.get_one_user_stat_from_db('casino_admin'), parse_mode='HTML')
                    bot.send_message(message.chat.id, db.get_one_user_stat_from_db(str(message.from_user.username)), parse_mode='HTML')
                if result_of_casino in array_of_procents_win:
                    bot.send_message(message.chat.id, f'Ты выиграл! +{str(rate)} рофлов')
                    bot.send_message(message.chat.id, f'обокрал Казиныча на {str(rate)} рофлов')
                    db.db_add_rofl(db.casino_admin, str(message.from_user.username), rate)
                    db.db_remove_rofl(str(message.from_user.username), db.casino_admin, rate)
                    bot.send_message(message.chat.id, db.get_one_user_stat_from_db('casino_admin'), parse_mode='HTML')
                    bot.send_message(message.chat.id, db.get_one_user_stat_from_db(str(message.from_user.username)), parse_mode='HTML')
                if result_of_casino in array_of_procents_lose:
                    bot.send_message(message.chat.id, f'Ты проиграл! -{str(rate)} рофлов')
                    bot.send_message(message.chat.id, f'Казиныч снова в выигрыше! casino_admin +{str(rate)} рофлов')
                    db.db_remove_rofl(db.casino_admin, str(message.from_user.username), rate)
                    db.db_add_rofl(str(message.from_user.username), db.casino_admin, rate)
                    bot.send_message(message.chat.id, db.get_one_user_stat_from_db('casino_admin'), parse_mode='HTML')
                    bot.send_message(message.chat.id, db.get_one_user_stat_from_db(str(message.from_user.username)), parse_mode='HTML')

                    db.db_upgrade_casino_time(str(message.from_user.username))



if __name__ == '__main__':
    db.start_bot()
    bot.infinity_polling()


    """
    TODO: 
    Удаление кучи сообщений из козиныча(?) по таймауту
    функция реагирования на сообщения "дай рофл" "дайте рофл" и т.д ДОПИСАТЬ
    вести бомжей в БД
    функция реагирования на событие улетания в минус рофлов пользователя
    рофлокредит
    запилить ранги
    DELAY НА СООБЗЩЕНИЯ
    """