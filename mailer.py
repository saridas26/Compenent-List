import os
import smtplib
from email.message import EmailMessage

def send_email(to_address, subject, body, attachment_path):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = os.getenv("MAIL_USERNAME")
    msg['To'] = to_address
    msg.set_content(body)

    with open(attachment_path, 'rb') as f:
        msg.add_attachment(
            f.read(),
            maintype='application',
            subtype='pdf',
            filename=os.path.basename(attachment_path)
        )

    with smtplib.SMTP('smtp.office365.com', 587) as smtp:
        smtp.starttls()
        smtp.login(os.getenv("MAIL_USERNAME"), os.getenv("MAIL_PASSWORD"))
        smtp.send_message(msg)
