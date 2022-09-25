import smtplib as smtp

class EnviarEmailSMTP():
    def __init__(self,server,port):
        self.SMTP_SERVER = server
        self.SMTP_PORT = port
    def enviar_email(self, de, senha, para, assunto, mensagem):
        para = para.split(",")
        mensagem = f"Subject: {assunto}\n\n{mensagem}".encode('utf-8')
        try:
            with smtp.SMTP(self.SMTP_SERVER,self.SMTP_PORT) as s:
                s.starttls()
                s.login(de, senha)
                s.sendmail(de, para, mensagem)
            print("E-mail enviado!")
        except Exception as erro:
            print("Não foi possível enviar o e-mail. Erro:", erro)
