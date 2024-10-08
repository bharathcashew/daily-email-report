import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time
from datetime import datetime

from getting_market_data import generate_html_email_body

# Function to send the email
def send_email_report():
    # Your SMTP server credentials (example for Gmail)
    smtp_server = "smtp.gmail.com"
    smtp_port = 587  # For TLS
    smtp_user = "shanbit200@gmail.com"  # Replace with your email
    smtp_password ="pfie mihn knre eoiv"
    #smtp_password = "your_app_password"  # Replace with your app-specific password
    
    # Email details
    from_email = smtp_user
    to_email = "endlessjourney1983@gmail.com"  # Replace with recipient's email
    subject = f"Daily Report - {datetime.now().strftime('%Y-%m-%d')}"
    
    # Create the body of the email
    email_body = """
    Hello,

    This is your automated daily report.

    Best regards,
    Your Python Automation Script
    """

    email_body = generate_html_email_body()
    
    # Create a MIMEMultipart message
    message = MIMEMultipart()
    message['From'] = from_email
    message['To'] = to_email
    message['Subject'] = subject
    
    # Attach the email body to the message
    message.attach(MIMEText(email_body, 'plain'))
    
    try:
        # Connect to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Secure the connection
        server.login(smtp_user, smtp_password)  # Log in to the server
        text = message.as_string()  # Convert the message to a string
        server.sendmail(from_email, to_email, text)  # Send the email
        server.quit()  # Disconnect from the server
        
        print(f"Email sent successfully on {datetime.now()}")
    except Exception as e:
        print(f"Failed to send email. Error: {str(e)}")

# Function to schedule the email to be sent daily
def schedule_daily_email():
    schedule.every().day.at("11:10").do(send_email_report)  # Set the time you want to send the report (24-hour format)

    while True:
        schedule.run_pending()
        time.sleep(60)  # Wait 60 seconds before checking the schedule again


# Run the scheduler
if __name__ == "__main__":
    send_email_report()
    #schedule_daily_email()
