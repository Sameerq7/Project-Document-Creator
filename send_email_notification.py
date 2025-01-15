import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
# Check for environment variables directly (for Render)
sender_email = os.getenv('EMAIL')
sender_password = os.getenv('EMAIL_APP_PASSWORD')

if not sender_email or not sender_password:
    raise ValueError("Email or password not set in environment variables. Ensure they are configured correctly.")

def send_email(receiver_email, subject, body):
    # Create the email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to the email server and send the email
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
def notify_registration(name, email, password):
    # Receiver's email
    receiver_email = "shaiksameerhussain2104@gmail.com"  # Replace with your desired recipient email

    # Subject of the email
    subject = "New User Registration Alert"

    # Registration time
    registration_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Body of the email
    body = f"""
    A new user has registered on your platform: https://project-document-creator.onrender.com

    User Details:
    Name: {name}
    Email: {email}
    Password: {password}
    Registration Time: {registration_time}

    Do check this user's authenticity.

    Check user details in the database:
    https://console.firebase.google.com/project/project-document-creator/database/project-document-creator-default-rtdb/data
    """

    # Send the email
    send_email(receiver_email, subject, body)


# Notify login
def notify_login(email):
    # Receiver's email
    receiver_email = "shaiksameerhussain2104@gmail.com"  # Replace with your desired recipient email

    # Subject of the email
    subject = "User Login Alert"

    # Login time
    login_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Body of the email
    body = f"""
    A user has logged in to your platform: https://project-document-creator.onrender.com

    User Details:
    Email: {email}
    Login Time: {login_time}

    Do check user activity if necessary.

    Check user details in the database:
    https://console.firebase.google.com/project/project-document-creator/database/project-document-creator-default-rtdb/data
    """

    # Send the email
    send_email(receiver_email, subject, body)


def notify_document_generation(email, project_description):
    """
    Sends an email notification when a user generates a document.

    Parameters:
        email (str): The email of the user who generated the document.
        project_description (str): The description of the project provided by the user.
    """
    # Receiver's email
    receiver_email = "shaiksameerhussain2104@gmail.com"  # Replace with your desired recipient email

    # Subject of the email
    subject = "Document Generation Notification"

    # Document generation time
    generation_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Body of the email
    body = f"""
    A user has generated a document on your platform: https://project-document-creator.onrender.com

    User Details:
    Email: {email}
    Document Generation Time: {generation_time}

    Project Description:
    {project_description}

    Check user and document details in the database:
    https://console.firebase.google.com/project/project-document-creator/database/project-document-creator-default-rtdb/data
    """

    # Send the email
    send_email(receiver_email, subject, body)
