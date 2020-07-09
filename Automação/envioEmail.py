#Importando bibliotecas
import smtplib

#Importando funções
from email.mime.multipart import MIMEMultipart #Auxilia na construção do email
from email.mime.text import MIMEText #Auxilia na construção do texto
from email.mime.base import MIMEBase 
from email import encoders

fromaddr = "lucasdutrabraz@gmail.com"
toaddr = "lucasdutrabraz@gmail.com, luksafadinho@gmail.com"

# Instância do MIMEMultipart
msg = MIMEMultipart()

#Estruturando o email
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Venha conhecer nosso restaurante!!!"
body = """Inauguração do nosso restaurante essa noite, venha conhecer."""
msg.attach(MIMEText(body, 'plain'))#Adiciona o body no email

#Servidor SMTP
s = smtplib.SMTP('smtp.gmail.com', 587)

# Segurança
s.starttls()

s.login(fromaddr, '1l2u3c4a5s')

# Converte para String
text = msg.as_string()

s.sendmail(fromaddr, toaddr, text)#Enviando o email

s.quit()