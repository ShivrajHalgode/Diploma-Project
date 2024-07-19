import smtplib

sender = "kingshivraj963@gmail.com"
pwd = "8421655251@svsmd"

try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender, pwd)
    print("Login successful!")
except smtplib.SMTPAuthenticationError as e:
    print(f"SMTP Authentication Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    server.quit()  # Ensure to quit the server connection
