# ### Enviando Email com Conteúdo HTML

from email.message import EmailMessage
import smtplib

EMAIL = 'gabrielfelippe90@gmail.com'
SENHA = input('Digite a senha do seu Email: ')

contacts = ['gabrielfelippe@outlook.com','akirascientist@gmail.com']

msg = EmailMessage()
msg['Subject'] = 'Teste'
msg['From'] = EMAIL
msg['To'] = ', '.join(contacts)

msg.set_content('Conteúdo em texto puro')
msg.add_alternative("""
<!DOCTYPE html>
<html>
    <body>
        <h1 style="color:MidnightBlue;">Email escrito em HTML!</h1>
    </body>
</html>
""", subtype='html')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL, SENHA)
    smtp.send_message(msg)
