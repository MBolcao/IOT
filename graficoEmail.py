from flask import Flask, render_template

import smtplib
from email.message import EmailMessage
import mimetypes

def sendEmail(destinatario, arquivo):
  # Cria a mensagem de email
  msg = EmailMessage()
  msg['From'] = 'devbolcao@gmail.com'
  msg['To'] = destinatario
  msg['Subject'] = 'Grafico de fluxo'
  msg.set_content('Segue gráfico com o fluxo de caixa')

  # Determina o tipo MIME do arquivo
  tipo_mime, _ = mimetypes.guess_type(arquivo)
  tipo_mime_principal, tipo_mime_sub = tipo_mime.split('/')
  
  # Abre o arquivo em modo binário e o anexa ao email
  with open(arquivo, 'rb') as arq:
    msg.add_attachment(arq.read(),
                       maintype=tipo_mime_principal,
                       subtype=tipo_mime_sub,
                       filename=arquivo)

  with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login('devbolcao@gmail.com', 'pjfv gpwc ctox symg')
    smtp.send_message(msg)

def enviarEmail(endereco):
  sendEmail(endereco,'images/grafico.png')
  return render_template("index.html")

