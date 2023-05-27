import smtplib, ssl
from mail import credentials
from email.mime.text import MIMEText
import os

class Mailer:
    context = ssl.create_default_context()
    port = 465
    assistent_login = str(os.getenv("assistent_login"))
    assistent_password = str(os.getenv("assistent_password"))

    # Create a secure SSL context
    def send_mail(self, recipient, msg: MIMEText):
        with smtplib.SMTP_SSL("smtp.gmail.com", self.port, context=self.context) as server:
            server.login(self.assistent_login, self.assistent_password)
            server.sendmail(self.assistent_login, recipient, msg.as_string())

