import smtplib #Libreria para enviar correos al cliente
import imaplib #Se encarga de mapear el correo, administrar que esta visto que no esta visto
import time
import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtp_server = 'smtp.gmail.com' #Definiendo que el servidor es, este servidor es del correo que va a dar la respuestas
smtp_port = 587 #Puerto estandar para smtp, se puede usar tambien el 993

imap_server = 'imap.gmail.com'

username = 'stephano.mejia1@gmail.com'
password = 'rhcjllqxabwnemhk'


def send_email(to,subject,body):
    server = smtplib.SMTP(smtp_server, smtp_port) 
    server.ehlo() #Hello World
    server.starttls() #Genera una conexion segura con el servidor
    server.login(username, password) #Loguear en el servidor
    
    msg = MIMEMultipart() #Establecer el mensaje
    
    msg['From'] = username
    msg['To'] = to
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain')) #Crear el mensaje en un texto plano
    server.sendmail(username, to, msg.as_string())
    
    server.quit() #Cerrando el servidor
    

def recive_email():
    mail = imaplib.IMAP4_SSL(imap_server) 
    mail.login(username, password)
    mail.select('inbox') #Seleccionando el buzon donde va a buscar
    
    
    #Asignacion doble de variables:
    
    _,search_data=mail.search(None, 'UNSEEN SUBJECT' "Practica") #Unseen subject = mensajes no vistos 
    
    #Para cada numero que haya en searchdata pos 0, separarlos uno por uno
    for num in search_data[0].split(): 
        _,email_Data = mail.fetch(num, '(RFC822)') #RFC822 estandar de encabezado de los correos
        _,b = email.data[0]
        email_message = email.message_from_bytes(b) #Va y busca que tiene los mensajes y toma el correo de quien viene, el asunto y el contenido
        subject = email.message('Subject') #Asignar el subject a la variable subject
        sender = email.message('From')
        print('El correo viene de : ', sender)
        print('Asunto: ', subject)
        
        response_subject = 'Hola'
        response_body = 'Su correo fue aceptado, le responderremos lo mas pronto'
        send_email(sender, response_subject, response_body)
        mail.store(num, '+FLAGS', '\\Seen')
        

while True:
    recive_email()
    print('Esperando 2 segundos')
    time.sleep(2)
    
    
    
    