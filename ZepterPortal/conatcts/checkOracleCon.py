import os

import cx_Oracle
import oracledb  # Вместо cx_Oracle

# Укажи путь к нужному Instant Client
oracle_client_path = r"H:\app\client\sholpan.baitursynova\product\12.2.0\client_1"

# Добавляем путь к Instant Client в PATH
os.environ["PATH"] = oracle_client_path + ";" + os.environ["PATH"]

# Инициализируем Oracle Client
oracledb.init_oracle_client(lib_dir=oracle_client_path)

# Настраиваем подключение
dsn = oracledb.makedsn("192.168.99.4", 1521, service_name="office")
conn = cx_Oracle.connect(user='soft', password='ghtldt4yst', dsn=dsn)
"""conn = oracledb.connect(dsn)"""

print("Успешное подключение!")


cursor = conn.cursor()

    # Выполняем SELECT-запрос
cursor.execute("select s.saradnik#,s.ime,s.iin,s.rodjen,s.telefon,s.cl100,s.activation_date from saradnik s where s.saradnik1='ZEPTER'")

    # Получаем данные
rows = cursor.fetchall()

    # Выводим результат
print("Данные из таблицы TEMP:")
for row in rows:
    print(row)

    # Закрываем курсор и соединение
cursor.close()
conn.close()
"""
except oracledb.DatabaseError as e:
    print(f"Ошибка подключения: {e}")
    
    
    
    

"""
