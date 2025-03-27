from fastapi import FastAPI
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_EMAIL ="pythonforsamir@gmail.com"
SMTP_PASSWORD="zflx vjqn zwmb spyo"

def send_mail(to_email:str,subject:str,text:str):
    msg = MIMEMultipart()
    msg['From'] = SMTP_EMAIL
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(text,'html'))
    
    #connect to mail server....
    server = smtplib.SMTP(SMTP_SERVER,SMTP_PORT)
    server.starttls()
    server.login(SMTP_EMAIL,SMTP_PASSWORD)
    server.sendmail(SMTP_EMAIL,to_email,msg.as_string())
    server.quit()
    
    return {"message":"Mail sent successfully"}

#send_mail("samir.vithlani83955@gmail.com","Test Mail","This is a test mail from fast...")
