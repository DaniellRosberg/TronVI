import subprocess
import time

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('cp866').split('\n')
WiFis = [line.split(':')[1]
          [1:-1] for line in data if "Все профили пользователей" in line]
for WiFi in WiFis:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', WiFi, 'key=clear']).decode('cp866').split(
        '\n')
    results = [line.split(':')[1]
               [1:-1] for line in results if "Содержимое ключа" in line]
    try:
        print(f'Имя сети: {WiFi}, Пароль: {results[0]}')
    except IndexError:
        print(f'Имя сети: {WiFi}, Пароль не найден!')

