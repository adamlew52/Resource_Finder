import os
from email.message import EmailMessage
import ssl
import smtplib

email_sender = "theceresapp@gmail.com"
email_pword = "fxfh hyeo oell jedw"
email_reciever = "adamsprojects412@gmail.com"

subject = "TEST SUBJECT"
body = """
TEST BODY NOT SURE WHY ITS SO BIG I LOVE TRIPLE QUOTES!!!
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_reciever
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_pword)
    smtp.sendmail(email_sender, email_reciever, em.as_string())