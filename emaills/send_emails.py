from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
import smtplib, requests, json
from email import encoders
from .template_emails import *
from company.models import Company

def Send_Email_Verified_Company(pk,token):
    company = Company.objects.get(pk = pk)
    remitente = 'facturacionelectronica2030t@gmail.com'
    destinatarios = [company.email]
    asunto = "Valida tu cuenta empresarial de MilHojasDeVidas"
    html = EMAIL_VERIFIED
    html = html.replace("$(company)", company.name)
    html = html.replace("$(url)", f"http://localhost:8000/user/verified_company/{pk}/{token}")
    mensaje = MIMEMultipart()
    mensaje['From'] = remitente
    mensaje['To'] = ", ".join(destinatarios)
    mensaje['Subject'] = asunto
    mensaje.attach(MIMEText(html,'html'))
    sesion_smtp = smtplib.SMTP('smtp.gmail.com', 587)
    sesion_smtp.starttls()
    texto = mensaje.as_string()
    usuario = 'facturacionelectronica2030@gmail.com'
    clave = 'webqbjzogcbqhtew'
    sesion_smtp.login(usuario,clave)
    sesion_smtp.sendmail(remitente, destinatarios, texto)
    sesion_smtp.quit()

