import sqlite3
import tabulate
import datetime


connect = sqlite3.connect('db.db', check_same_thread=False)
cursor = connect.cursor()
casino_admin = 'casino_admin'

def start_bot():
    cursor.execute("""CREATE TABLE IF NOT EXISTS users (
                username text, 
                roflancoins_balance int, 
                given_plus_count int, 
                given_minus_count int,
                received_plus_count int,
                received_minus_count int,
                last_rofl_action text,
                last_casino_action text
                )""")
    connect.commit()

    cursor.execute(f"SELECT username FROM users WHERE username = '{casino_admin}'")
    dt = datetime.datetime.now()
    if cursor.fetchone() is None:
        cursor.execute(f"INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (casino_admin, 1000, 0, 0, 0, 0, dt, dt) )

    connect.commit()


def add_new_user_to_db(username):
    cursor.execute(f"SELECT username FROM users WHERE username = '{username}'") 
    dt = datetime.datetime.now()
    if cursor.fetchone() is None:
        cursor.execute(f"INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (username, 10, 0, 0, 0, 0, dt, dt) )
        connect.commit()

def get_users_stat_from_db():
    cursor.execute("SELECT username, roflancoins_balance FROM users ORDER BY roflancoins_balance DESC")

    rows = cursor.fetchall()

    str_to_telegram = tabulate.tabulate(rows, tablefmt="pipe")
    str_to_telegram = f"<pre>{str_to_telegram}</pre>"
    return str_to_telegram


def get_one_user_stat_from_db(username):
    cursor.execute(f"SELECT username, roflancoins_balance FROM users WHERE username = '{username}'")

    userstat = cursor.fetchall()

    userstat = tabulate.tabulate(userstat, tablefmt="pipe")
    userstat = f"<pre>{userstat}</pre>"

    return userstat

def get_roflanbalance_from_db(username):
    cursor.execute(f"SELECT roflancoins_balance FROM users WHERE username = '{username}'")
    balance = cursor.fetchone()
    dt = datetime.datetime.now()
    if balance is None:
        cursor.execute(f"INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (username, 10, 0, 0, 0, 0, dt, dt) )
        connect.commit()
    cursor.execute(f"SELECT roflancoins_balance FROM users WHERE username = '{username}'")
    balance = cursor.fetchone()
    balance = int(balance[0])
    
    return balance


def db_add_rofl(from_user, to_user, count):

    # проверяем, что user есть в БД. Если нету, добавляем
    cursor.execute(f"SELECT username FROM users WHERE username = '{to_user}'")
    if cursor.fetchone() is None:
        add_new_user_to_db(to_user)

    cursor.execute(f"SELECT username FROM users WHERE username = '{from_user}'")
    if cursor.fetchone() is None:
        add_new_user_to_db(from_user)

    for i in cursor.execute(f"SELECT roflancoins_balance, received_plus_count FROM users WHERE username = '{to_user}'"):
        roflancoins_balance = i[0]
        received_plus_count = i[1]

        cursor.execute(f"UPDATE users SET roflancoins_balance = {roflancoins_balance + count} WHERE username = '{to_user}'")
        connect.commit()
        cursor.execute(f"UPDATE users SET received_plus_count = {received_plus_count + count} WHERE username = '{to_user}'")
        connect.commit()

    for i in cursor.execute(f"SELECT given_plus_count FROM users WHERE username = '{from_user}'"):
        given_plus_count = i[0]

        cursor.execute(f"UPDATE users SET given_plus_count = {given_plus_count + count} WHERE username = '{from_user}'")
        connect.commit()

def db_remove_rofl(from_user, to_user, count):

    # проверяем, что user есть в БД. Если нету, добавляем
    cursor.execute(f"SELECT username FROM users WHERE username = '{to_user}'")
    if cursor.fetchone() is None:
        add_new_user_to_db(to_user)

    cursor.execute(f"SELECT username FROM users WHERE username = '{from_user}'")
    if cursor.fetchone() is None:
        add_new_user_to_db(from_user)

    for i in cursor.execute(f"SELECT roflancoins_balance, received_minus_count FROM users WHERE username = '{to_user}'"):
        roflancoins_balance = i[0]
        received_minus_count = i[1]

        cursor.execute(f"UPDATE users SET roflancoins_balance = {roflancoins_balance - count} WHERE username = '{to_user}'")
        connect.commit()
        cursor.execute(f"UPDATE users SET received_minus_count = {received_minus_count + count} WHERE username = '{to_user}'")
        connect.commit()

    for i in cursor.execute(f"SELECT given_minus_count FROM users WHERE username = '{from_user}'"):
        given_minus_count = i[0]

        cursor.execute(f"UPDATE users SET given_minus_count = {given_minus_count + count} WHERE username = '{from_user}'")
        connect.commit()

def db_upgrade_rofl_time(username):

    now_time = datetime.datetime.now()

    cursor.execute(f"UPDATE users SET last_rofl_action = '{now_time}' WHERE username = '{username}'")
    connect.commit()

def db_upgrade_casino_time(username):

    now_time = datetime.datetime.now()

    cursor.execute(f"UPDATE users SET last_casino_action = '{now_time}' WHERE username = '{username}'")
    connect.commit()
    
def db_get_rofl_time(username):

    cursor.execute(f"SELECT last_rofl_action FROM users WHERE username = '{username}'")
    last_casino_action = cursor.fetchone()

    return last_rofl_action

def db_get_casino_time(username):

    cursor.execute(f"SELECT last_casino_action FROM users WHERE username = '{username}'")
    last_casino_action = cursor.fetchone()

    last_casino_action = last_casino_action[0]
    last_casino_action = datetime.datetime.strptime(last_casino_action, '%Y-%m-%d %H:%M:%S.%f')

    return last_casino_action