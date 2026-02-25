import smtplib
from email.message import EmailMessage

def Send_mail(sender, app_password, receiver, subject, body):
    
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
    sender_email = "thorattanmay2004@gmail.com"      
    app_password = "askndssdksmcw"    
    receiver_email = "testing08@gmail.com"
    
    subject = "Testing Mail"
    body = """Hello,
    Tanmay Thorat This Side
    Thanks for reading! """

    Send_mail(sender_email, app_password, receiver_email, subject, body)
    print("Mail sent successfully.")

if __name__ == "__main__":
    main()
