from dotenv import load_dotenv
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Load environment variables
load_dotenv()

def send_email(receiver_email, subject, body):
    sender_email = os.getenv('EMAIL')  # Fetch sender email
    sender_password = os.getenv('EMAIL_APP_PASSWORD')  # Fetch app password

    if not sender_email or not sender_password:
        raise ValueError("Email or password not set in environment variables.")

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        mail.login(sender_email, sender_password)
        mail.sendmail(sender_email, receiver_email, msg.as_string())
        mail.close()

        print(f"Email sent successfully to {receiver_email}!")
    except smtplib.SMTPAuthenticationError:
        print('Authentication failed. Check your email credentials.')
    except smtplib.SMTPException as e:
        print(f'Failed to send email. Error: {e}')


# Notify registration
def notify_registration(name, email, password, custom_link):
    receiver_email = "shaiksameerhussain2104@gmail.com"  # Replace with your email
    subject = "New User Registration Alert"
    body = f"""
    A new user has registered:

    Name: {name}
    Email: {email}
    Password: {password}

    View more details or take action here:
    {custom_link}
    """
    send_email(receiver_email, subject, body)


# Test the function
if __name__ == "__main__":
    name = "John Doe"
    email = "johndoe@example.com"
    password = "password123"
    custom_link = "https://example.com/user-details"

    notify_registration(name, email, password, custom_link)
