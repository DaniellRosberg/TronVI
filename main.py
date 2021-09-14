import socket
from requests import get
from getpass import getpass

import FUCKING_INVALID_send_mail

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
public_ip = get('http://api.ipify.org').text
email_text = (f'Host: {hostname}\nLocal IP: {local_ip}\nPublic IP: {public_ip}')

FUCKING_INVALID_send_mail.send_mail(email_text)

print('END SCRIPT')