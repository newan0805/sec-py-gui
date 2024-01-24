import smtplib
from email.mime.text import MIMEText

# wloi ncbk unjb vvob

def send_otp_email(receiver_email, otp):
        sender_email = "newan2003test@gmail.com"  # Replace with your email
        sender_password = "Newan@071"  # Replace with your email password

        message = f"Subject: OTP for SignUp\n\nYour OTP is: {otp}"

        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(sender_email, sender_password)
                server.sendmail(sender_email, receiver_email, message)

            print("OTP sent successfully!")
        except Exception as e:
            print(f"Error sending OTP: {e}")
            
            
# send_otp_email('newan0805@gmail.com','otp:xxxxxxxx')

import smtplib
import ssl
from email.message import EmailMessage

# Define email sender and receiver
email_sender = 'newan2003test@gmail.com'
email_password = 'wloi ncbk unjb vvob'
email_receiver = 'newan0805@gmail.com'

# Set the subject and body of the email
subject = 'Check out my new video!'
body = """
Test: Check
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

# Add SSL (layer of security)
context = ssl.create_default_context()

# Log in and send the email
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())