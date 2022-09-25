# ## Por meio do SMTPLIB AKIRADEV
# Fonte: https://akiradev.netlify.app/posts/enviando-emails-python/#:~:text=A%20Biblioteca%20smtplib%20O%20m%C3%B3dulo%20smtplib%20define%20um,Protocol%29%20e%20o%20RFC%201869%20%28SMTP%20Service%20Extensions%29.

# ### Enviando Email Plain-Text

from email.message import EmailMessage
import smtplib

#EMAIL = 'gabrielfelippe90@gmail.com'
EMAIL = ""
#SENHA = input('Digite a senha do seu Email: ')
SENHA = ""
SMTP_USERNAME = ""
SMTP_PASSWORD = ""

msg = EmailMessage()
msg['Subject'] = 'Linguagem Python'
msg['From'] = EMAIL
msg['To'] = ''
msg.set_content('Contéudo do Email enviado com Python!')
#print(msg)

with smtplib.SMTP_SSL("smtp.office365.com", 587) as smtp:
    smtp.login(EMAIL, SENHA)
    smtp.send_message(msg)

smtp = smtplib.SMTP("smtp.office365.com",587)
smtp.login(SMTP_USERNAME,SMTP_PASSWORD)
smtp.send_message(msg)
