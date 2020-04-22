import paramiko
import sqlite3

print('beta 0.1')

conn = sqlite3.connect(r"C:\Users\alexy\OneDrive\Рабочий стол\database\database.db3") # Connect к базе
cursor = conn.cursor()

block = input('Введите блок   ') # Выборка по блоку
sql = 'SELECT ip FROM servers WHERE block=' + block
for row in cursor.execute(sql): # Функция записи в столб перебирая серверы
# print(cursor.fetchall()) # Вывод в строку запроса
    print(row) # Вывод строк


# ### user menu ###
# user_menu = input('1. Создать пользователя \n'
# '2. Назначить права \n'
# '3. Проверить nginx \n'
# '4. Создать каталог \n'
# '5. Сменить владельца каталога')
#
#
# host = '192.168.153.129'
# user = user_name
# secret = secret
# port = 22
#
# ssh = paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect(hostname=host, username=user, password=secret, port=port)
#
# stdin, stdout, stderr = ssh.exec_command("ls -la / | grep gateway")
# see_SPO = stdout.readline()
# print(see_SPO)
# ssh.close()