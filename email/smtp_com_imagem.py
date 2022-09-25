# ### Enviando Email com Imagens

from email.message import EmailMessage
import smtplib
import imghdr

EMAIL = 'gabrielfelippe90@gmail.com'
SENHA = input('Digite a senha do seu Email: ')

msg = EmailMessage()
msg['Subject'] = 'Teste'
msg['From'] = EMAIL
msg['To'] = 'gabrielfelippe@outlook.com'
msg.set_content('Imagem anexada')

files = ['imagem.jpg','imagem2.jpg']

for file in files:
    with open(file, 'rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name

    msg.add_attachment(file_data, 
        maintype='image', 
        subtype=file_type,
        filename=file_name
    )

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL, SENHA)
    smtp.send_message(msg)
