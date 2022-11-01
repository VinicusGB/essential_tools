import smtplib
from email.message import EmailMessage


class EnviarEmailSMTP():
    """Enviar e-mail SMTP"""
    def __init__(self,server=SMTP_SERVER,port=SMTP_PORT,senha=SMTP_PASSWORD,email=SMTP_USERNAME):
        self.SMTP_SERVER = server
        self.SMTP_PORT = port
        self.PASSWORD = senha
        self.USERNAME = email
    def testar_conexao(self):
        print(self.SMTP_SERVER,self.SMTP_PORT)
        with smtplib.SMTP(self.SMTP_SERVER,self.SMTP_PORT) as smtp_teste:
            print(smtp_teste.starttls())
            print(smtp_teste.login(self.USERNAME,self.PASSWORD))
    def enviar_simples(self,EMAIL_FROM,EMAIL_SUBJECT,EMAIL_MESSAGE):
        MESSAGE = f"Subject: {EMAIL_SUBJECT}\n\n{EMAIL_MESSAGE}".encode('utf-8')
        try:
            with smtplib.SMTP(self.SMTP_SERVER,self.SMTP_PORT) as s:
                s.starttls()
                s.login(self.USERNAME,self.PASSWORD)
                s.sendmail(self.USERNAME,EMAIL_FROM,MESSAGE)
            print("E-mail enviado!")
        except Exception as erro:
            print("Não foi possível enviar o e-mail. Erro:", erro)
    def enviar_com_arquivos(self,EMAIL_FROM,EMAIL_SUBJECT,EMAIL_MESSAGE,FILES=[],HTML_CONTENT=False):
        MESSAGE = EmailMessage()
        MESSAGE['Subject'] = EMAIL_SUBJECT
        MESSAGE['From'] = self.USERNAME
        MESSAGE['To'] = EMAIL_FROM.split(",")
        if HTML_CONTENT:
            MESSAGE.add_alternative(f"<!DOCTYPE html><html><body>{EMAIL_MESSAGE}</body></html>",subtype='html')
        else:
            MESSAGE.set_content(EMAIL_MESSAGE)
        for file in FILES:
            with open(file,'rb') as f:
                file_data = f.read()
                file_name = f.name
            MESSAGE.add_attachment(file_data, 
                maintype='application', 
                subtype='octet-stream',
                filename=file_name
            )
        try:
            with smtplib.SMTP(self.SMTP_SERVER,self.SMTP_PORT) as s:
                s.starttls()
                s.login(self.USERNAME,self.PASSWORD)
                s.send_message(MESSAGE)
            print("E-mail enviado!")
        except Exception as erro:
            print("Não foi possível enviar o e-mail. Erro:", erro)
    def enviar_html(self,EMAIL_FROM,EMAIL_SUBJECT,EMAIL_MESSAGE,HTML_CONTENT=False):
        MESSAGE = EmailMessage()
        MESSAGE['Subject'] = EMAIL_SUBJECT
        MESSAGE['From'] = self.USERNAME
        MESSAGE['To'] = EMAIL_FROM.split(",")
        if HTML_CONTENT:
            MESSAGE.add_alternative(f"<!DOCTYPE html><html><meta charset='utf-8'/><body>{EMAIL_MESSAGE}</body></html>",subtype='html')
        else:
            MESSAGE.set_content(EMAIL_MESSAGE)
        try:
            with smtplib.SMTP(self.SMTP_SERVER,self.SMTP_PORT) as s:
                s.starttls()
                s.login(self.USERNAME,self.PASSWORD)
                s.send_message(MESSAGE)
            print("E-mail enviado!")
        except Exception as erro:
            print("Não foi possível enviar o e-mail. Erro:", erro)
