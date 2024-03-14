import os
from dotenv import load_dotenv
from pathlib import Path
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

load_dotenv()
os.system('cls')

caminho = Path(__file__).parent/'aula303.html'
remetente = os.getenv('FROM_EMAIL', '')
destinatarios = ['vg452004@gmail.com', 'matheusfernando040@gmail.com',
'lukascalazans12@gmail.com']

smtp_server = os.getenv('SMTP_SERVER','')
smtp_port = 587
smtp_user = os.getenv('FROM_EMAIL', '')
smtp_password = os.getenv('EMAIL_PASSWORD','')

with open(caminho, 'r', encoding='utf8') as arquivo:
    texto = arquivo.read()
    template = Template(texto)
    texto_email = template.substitute(nome = 'Vítor' )

email = MIMEMultipart()
email['From'] = remetente
email['To'] = ', '.join(destinatarios)
email['Subject'] = 'Enviando email com Python'

corpo_html = MIMEText(texto_email, 'html', 'utf8')
email.attach(corpo_html)

with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.ehlo()
    server.starttls()
    server.login(smtp_user, smtp_password)
    server.send_message(email)
    print('EMAIL ENVIADO COM SUCESSO')