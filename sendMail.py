from email import message
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# from email.message import EmailMessage
username = "support@tecrun.tech"
    # username = input("Type your username and press enter: ")
password = "nova@0144" 
# message = EmailMessage()
# message['From'] = "noedmale@gmail.com" 
# message['To'] = "usjadon19@gmail.com"
# message['Subject'] = "Hey"
# message.set_content = " Go"
def takeEmailInput():
    # It takes microphone input from the user and returns string output.
    # speak('Enter Text For Email')
    inputString = input('Enter Text For Email:')
    return inputString

def sendEmail(to, content):
    port = 587  # For SSL

    # password = input("Type your password and press enter: ")
    context = ssl.create_default_context()
    # with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    #     server.login(username, password)
    #     # TODO: Send email here
    #     server.sendmail(username, to, content)
    with smtplib.SMTP_SSL("smtp.office365.com", port, context=context) as server:
        server.login(username, password)
        # TODO: Send email here
        server.sendmail(username, to, content)

def sendEmail_g(to, content):
    port = 587  # For starttls
    smtp_server = "smtp.office365.com"
    sender_email = username
    receiver_email = to
    # password = password
    message = content
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        try:
            server.sendmail(sender_email, receiver_email, message)
            print("Message sent successfully")
        except:
            print("Failed to send message")
            server.quit()
        
    # server = smtplib.SMTP('smtp.office365.com:587')
    # server.ehlo()
    # server.starttls()
    # server.login(username, password) #  Exception here
    # try:
    #     server.sendmail(username, to, content)
    #     print("Message sent successfully")
    # except:
    #     print("Failed to send message")
    # server.quit()

content = takeEmailInput()
to = "utkarsh2110024@akgec.ac.in"
sendEmail_g(to, content)

