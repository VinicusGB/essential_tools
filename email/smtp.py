# ## Por meio do SMTPLIB AKIRADEV
# Fonte: https://akiradev.netlify.app/posts/enviando-emails-python/#:~:text=A%20Biblioteca%20smtplib%20O%20m%C3%B3dulo%20smtplib%20define%20um,Protocol%29%20e%20o%20RFC%201869%20%28SMTP%20Service%20Extensions%29.

import smtplib

# configurações principais
#SMTP_SERVER = "smtp.gmail.com"
SMTP_SERVER = ""
#SMTP_PORT = 587
SMTP_PORT = 587
#SMTP_USERNAME = "sender_username_here@gmail.com"
SMTP_USERNAME = ""
#SMTP_PASSWORD = "sender_password_here"
SMTP_PASSWORD = ""
#EMAIL_FROM = "sender_username_here@gmail.com"
EMAIL_FROM = ""
#EMAIL_TO = "receiver_username_here@gmail.com"
EMAIL_TO = ""
#EMAIL_SUBJECT = "Attention:Subject here"
EMAIL_SUBJECT = "Teste Python"
EMAIL_MESSAGE = "The message here"
#EMAIL_MESSAGE = "Este é um e-mail de teste em Python"

s = smtplib.SMTP(SMTP_SERVER,SMTP_PORT)

s.starttls()

s.login(SMTP_USERNAME,SMTP_PASSWORD)

message = 'Subject: {}\n\n{}'.format(EMAIL_SUBJECT, EMAIL_MESSAGE)

s.sendmail(EMAIL_FROM, EMAIL_TO, message)

s.quit()
