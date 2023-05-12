from email.mime.base import MIMEBase
import smtplib

from constant import *
from stream import read_list

from pathlib import Path
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders

def send_email(to_address, subject, text, file_path: list):
    smtp_conf = read_list(SMTP_PATH)
    
    msg = MIMEMultipart()
    
    msg['From'] = smtp_conf[2]
    msg['To'] = to_address
    msg['Subject'] = subject

    msg.attach(MIMEText(text))

    for path in file_path:
        try:
            file = open(path, 'rb')
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(file.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment; filename={}'.format(Path(path).name))
            msg.attach(part)
            file.close()
        except IOError:
            continue

    smtp = smtplib.SMTP_SSL(smtp_conf[0], int(smtp_conf[1]))
    smtp.login(smtp_conf[2], smtp_conf[3])
    smtp.send_message(msg)
    smtp.quit()
