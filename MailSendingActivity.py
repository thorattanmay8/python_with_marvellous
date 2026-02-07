import smtplib
from email.message import EmailMessage

def Marvellous_send_mail(sender, app_password, receiver, subject, body):
    
    msg = EmailMessage()
    
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject
    
    msg.set_content(body)
    
    smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    
    smtp.login(sender, app_password)
    
    smtp.send_message(msg)
    
    smtp.quit()

def main():
    sender_email = "python.test@gmail.com"      
    app_password = "xxxxx xxxx xxxx xxxx"    
    receiver_email = "yourpersonalemail@gmail.com"
    
    subject = "Test Mail from Python Script"
    body = """Jay Ganesh,
    This is a test email sent using Marvellous Python.
    Regards,
    Marvellous Infosystems"""

    Marvellous_send_mail(sender_email, app_password, receiver_email, subject, body)
    print("Marvellous Mail Sent Successfully")

if __name__ == "__main__":
    main()
