import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email credentials
sender = "kingshivraj963@gmail.com"
password = "8421655251@svsmd"  # Use app-specific password if 2-Step Verification is enabled
recipient = "halgodeshivraj03@gmail.com"

# Email content
msg = MIMEMultipart()
msg['From'] = sender
msg['To'] = recipient
msg['Subject'] = "Test Email"
body = "This is a test email."
msg.attach(MIMEText(body, 'plain'))

try:
    # Set up the SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()  # Secure the connection
    server.login(sender, password)

    # Send the email
    text = msg.as_string()
    server.sendmail(sender, recipient, text)
    print("Email sent successfully!")

except smtplib.SMTPAuthenticationError as e:
    print(f"SMTP Authentication Error: {e}")
except Exception as e:
    print(f"Failed to send email: {e}")
finally:
    server.quit()
