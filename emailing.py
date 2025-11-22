import smtplib
import imghdr

from email.message import EmailMessage

password='pyno rwag cfdo jnmi'
account='sree0987h@gmail.com'
def send_email(email_img):
    email_message=EmailMessage()
    email_message['subject']='movement alert'
    email_message.set_content('new customer have arrived')


    with open(email_img,'rb') as file:
        content=file.read()
    email_message.add_attachment(content,maintype='image',subtype=imghdr.what(None,content))

    gmail=smtplib.SMTP('smtp.gmail.com',port=587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(account,password)
    gmail.sendmail(account,account,email_message.as_string())
    gmail.quit()
if __name__=='__main__':
    send_email(email_img='files/107.png')

