import smtplib as smtp

import socket

from getpass import getpass

from requests import get

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
public_ip = get('http://api.ipify.org').text
email = 'faxtrotuniform@yandex.ru'
password = 'Charley'
dest_email = 'alexandr9514@yandex.ru'
subject = 'IP'
email_text = (f'Host: {hostname}\nLocal IP: {local_ip}\nPublic IP: {public_ip}')
message = 'From: {}\nTo: {}\nSubject: {}\n\n{}'.format(email, dest_email, subject, email_text)
server = smtp.SMTP_SSL('smtp.yandex.com')

server.set_debuglevel(1)
server.ehlo(email)
server.login(email, password)
server.auth_plain()
server.sendmail(email, dest_email, message)
server.quit()