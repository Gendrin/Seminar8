# Создаем таблицы БД 1. Таблица клиентов и мастеров
# id / Name / SureName / Phone / Maser or Client (boolean - 1 client 0 - master) - users
# Таблица предварительной записи
# id / id_master / id_client / start_time / end_time - records
#Табица реально оказанных услуг
# id / id_master / id_client / id_sevice /start_time - orders
#Таблица видов оказываемых услуг
# id / name_service / cost - service
# Предварительная структура БД
import sqlite3

def CreateDB():
    connect = sqlite3.connect('barbershop.db')
    cursor = connect.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS users(
       id INT PRIMARY KEY,
       fname TEXT,
       lname TEXT,
       phone INT,
       typus INT);
    """)

    cursor.execute("""CREATE TABLE IF NOT EXISTS records(
           id INT PRIMARY KEY,
           id_master INT,
           id_client INT,
           start_time TEXT,
           end_time TEXT);
        """)

    cursor.execute("""CREATE TABLE IF NOT EXISTS service(
               id INT PRIMARY KEY,
               name_s TEXT,
               cost INT);
            """)

    cursor.execute("""CREATE TABLE IF NOT EXISTS orders(
               id INT PRIMARY KEY,
               id_master INT,
               id_client INT,
               id_service INT,
               start_time TEXT);
            """)
    connect.commit()

