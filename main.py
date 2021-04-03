import telebot
from random import randint # для казиныча
import time
import db


TOKEN = '1710589285:AAGPBaALjUILIyaRh39K-sushILAETlz8G8'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['balance'])
def send_users_stat(message):
	bot.reply_to(message, db.get_users_stat_from_db(), parse_mode='HTML')

@bot.message_handler(commands=['update'])
def send_update(message):
	bot.reply_to(message, "04.04.2021. Добавил Мегарофл, Мегаминус и Гучи линзы. Сделал казино с рандомным количеством рофлов. TODO: сделать ставки для казино. Хранить состояние, чтоб не спамили всякие Жени и не было голладского штурвала. Сделать ранги.")

@bot.message_handler(commands=['casino'])
def casino(message):
    balance = db.get_roflanbalance_from_db(str(message.from_user.username))
    if balance <= 0:
        bot.send_message(message.chat.id, 'На что играть собрался? Баланс нулевой')
    else:
        bot.reply_to(message, "Ставка поставлена!")
        time.sleep(2)
        bot.send_message(message.chat.id, "Ставок больше нет")
        time.sleep(2)
        bot.send_message(message.chat.id, "Кручу...")
        time.sleep(2)
        bot.send_message(message.chat.id, "Верчу...")
        time.sleep(2)
        bot.send_message(message.chat.id, "Наебать хочу!")
        time.sleep(2)
        result_of_casino = randint(1,2)
        roflan_count = randint(1, 10)
        if result_of_casino == 1:
            bot.reply_to(message, f"Проебал {roflan_count} рофлов!")
            db.db_remove_rofl(db.casino_admin, str(message.from_user.username), roflan_count)
        if result_of_casino == 2:
            bot.reply_to(message, f"Выиграл {roflan_count} рофлов!")
            db.db_add_rofl(db.casino_admin, str(message.from_user.username), roflan_count)

@bot.message_handler(regexp="^[+]")
def add_rofl_when_reply(message):
    if message.reply_to_message is not None:
        if message.from_user.username == message.reply_to_message.json['from']['username']:
            bot.reply_to(message, 'Сам себя плюсуешь? Думал наебать меня?')
        else:
            random_rofl = randint(1,20)
            if random_rofl == 1:
                bot.send_message(message.chat.id, 'Еееееебать! МЕГАРОФЛ!')
                bot.send_message(message.chat.id, '@' + message.from_user.username + ' дал МЕГАРОФЛ ' + '@' + message.reply_to_message.json['from']['username'])
                db.db_add_rofl(str(message.from_user.username), str(message.reply_to_message.json['from']['username']), 5)
                bot.send_message(message.chat.id, db.get_one_user_stat_from_db(str(message.reply_to_message.json['from']['username'])), parse_mode='HTML')
            else:
                bot.send_message(message.chat.id, '@' + message.from_user.username + ' дал рофлан ' + '@' + message.reply_to_message.json['from']['username'])
                db.db_add_rofl(str(message.from_user.username), str(message.reply_to_message.json['from']['username']), 1)
                bot.send_message(message.chat.id, db.get_one_user_stat_from_db(str(message.reply_to_message.json['from']['username'])), parse_mode='HTML')

@bot.message_handler(regexp="^[-]")
def remove_rofl_when_reply(message):
    if message.reply_to_message is not None:
        if message.from_user.username == message.reply_to_message.json['from']['username']:
            bot.reply_to(message, 'ХАХА тут долбаеб сам себе минусы ставит')
        else:
            random_rofl = randint(1,3)
            if random_rofl == 1:
                bot.send_message(message.chat.id, 'Еееееебать! МЕГАМИНУС!')
                bot.send_message(message.chat.id, '@' + message.from_user.username + ' залил МЕГАМИНУС ' + '@' + message.reply_to_message.json['from']['username'])
                db.db_remove_rofl(str(message.from_user.username), str(message.reply_to_message.json['from']['username']), 5)
                bot.send_message(message.chat.id, db.get_one_user_stat_from_db(str(message.reply_to_message.json['from']['username'])), parse_mode='HTML')
            elif random_rofl == 2:
                bot.send_message(message.chat.id, 'ГУЧИ ЛИНЗЫ ОТРАЗИЛИ ХЕЙТ')
                bot.send_message(message.chat.id, '@' + message.from_user.username + ' ОТРАЗИЛ ХЕЙТ ' + '@' + message.reply_to_message.json['from']['username'])
                db.db_remove_rofl(str(message.reply_to_message.json['from']['username']), str(message.from_user.username), 5)
                bot.send_message(message.chat.id, db.get_one_user_stat_from_db(str(message.from_user.username)), parse_mode='HTML')
            else:
                bot.send_message(message.chat.id, '@' + message.from_user.username + ' залил соляры ' + '@' + message.reply_to_message.json['from']['username'])
                db.db_remove_rofl(str(message.from_user.username), str(message.reply_to_message.json['from']['username']), 1)
                bot.send_message(message.chat.id, db.get_one_user_stat_from_db(str(message.reply_to_message.json['from']['username'])), parse_mode='HTML')

                

if __name__ == '__main__':
    bot.infinity_polling()