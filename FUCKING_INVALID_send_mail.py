import smtplib as smtp

import utils
from utils.smtp_utils import *



# SMTP-сервер Яндекса



server = smtp.SMTP_SSL(utils.smtp_utils.smtp_yandex)
def send_mail(parameter):
    server.set_debuglevel(1)
    server.ehlo(email)
    password = 'Charley'  #todo разобраться со скрытием пароля
    server.login(email, password)
    server.auth_plain()
    server.sendmail(email, dest_email, parameter)
    server.quit()