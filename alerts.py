import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config import EMAIL_SENDER, EMAIL_RECEIVER, APP_PASSWORD


def send_alert(metric_name, value):
     msg = MIMEMultipart()
     msg['From'] = EMAIL_SENDER
     msg['To'] = EMAIL_RECEIVER
     msg['Subject'] = "VM Metric alert"

     body = f"WARNING: {metric_name} is at {value:.2f}%\nPLEASE CHECK VM MERTICS"
     msg.attach(MIMEText(body, 'plain', 'utf-8'))


     try:
    # Use port 587 for STARTTLS
          with smtplib.SMTP("smtp.gmail.com", 587) as server:
              server.starttls() # Secure the connection
              server.login(EMAIL_SENDER, APP_PASSWORD)
              server.send_message(msg) # Standard way to send MIME objects
          print("Email sent successfully!")
     except Exception as e:
          print(f"Error: {e}")
