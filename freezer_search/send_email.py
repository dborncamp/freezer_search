import smtplib
import ssl
import os
from email.message import EmailMessage


def send_email(item_num, url, receiver):
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "borncampdev@gmail.com"
    password = os.getenv('DEVPASS')
    print(password)

    msg = EmailMessage()
    # me == the sender's email address
    # you == the recipient's email address
    msg['Subject'] = f'A Freezer on {url} may be available'
    msg['From'] = sender_email
    msg['To'] = receiver

    message = """\
    
    Item # {} may be available, please check it on: {}""".format(item_num, url)
    msg.set_content(message)

    print(msg)

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.send_message(msg)
        # server.sendmail(sender_email, receiver, msg)
