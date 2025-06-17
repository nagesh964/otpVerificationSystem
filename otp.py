import random
import smtplib
from email.mime.text import MIMEText
import re

def send_otp(user_email, sender_email, sender_password):
    otp = random.randint(100000, 999999)
    subject = "Your OTP Code"
    body = f"Your OTP code is {otp}"

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = user_email

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.starttls()
            smtp.login(sender_email, sender_password)
            smtp.sendmail(sender_email, user_email, msg.as_string())
        print("OTP has been sent to your email.")
    except Exception as e:
        print(f"Failed to send email: {e}")
        exit()

    return otp

def verify_otp(otp): 
    attempts = 3
    while attempts > 0:
        entered_otp = input("Enter the OTP: ")
        if str(otp) == entered_otp:
            print("OTP verified successfully!")
            return
        else:
            attempts -= 1
            print(f"Incorrect OTP. {attempts} attempt(s) left.")
    print("Too many incorrect attempts. Try again after 24 hours.")

def main():
    user_email = input("Please enter your email address: ")
    if not re.match(r"[^@]+@[^@]+\.[^@]+", user_email):
        print("Invalid email format.")
        return

    sender_email = "nkethavath83@gmail.com"
    sender_password = "wbws yzcy wpew tqey" 

    otp = send_otp(user_email, sender_email, sender_password)
    verify_otp(otp)

if __name__ == "__main__":
    main()
