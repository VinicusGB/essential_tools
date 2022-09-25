# ### Enviando Email com Arquivos PDF

from email.message import EmailMessage
import smtplib

EMAIL = 'gabrielfelippe90@gmail.com'
SENHA = input('Digite a senha do seu Email: ')

contacts = ['gabrielfelippe@outlook.com','akirascientist@gmail.com']

msg = EmailMessage()
msg['Subject'] = 'Teste'
msg['From'] = EMAIL
msg['To'] = ', '.join(contacts)
msg.set_content('Livro em Anexo')

files = ['Simulacra_and_Simulation.pdf','Neuromancer.pdf']

for file in files:
    with open(file, 'rb') as f:
        file_data = f.read()
        file_name = f.name

    msg.add_attachment(file_data, 
        maintype='application', 
        subtype='octet-stream',
        filename=file_name
    )

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL, SENHA)
    smtp.send_message(msg)
