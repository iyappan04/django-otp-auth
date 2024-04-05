import random
import string
from django.core.mail import send_mail
from django.conf import settings
from twilio.rest import Client

def generate_otp(length=6):
    characters = string.digits
    otp = ''.join(random.choice(characters) for _ in range(length))
    return otp

def send_otp_email(email, otp):
    subject = 'Your OTP for Login'
    message = f'Your OTP is: {otp}'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)
    

def send_otp_phone(phone_number, otp):
    account_sid = settings.TWILIO_SID 
    auth_token = settings.TWILIO_AUTH_TOKEN  
    twilio_phone_number = settings.TWILIO_AUTH_MOBILE 

    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=f'Your OTP is: {otp}',
        from_=twilio_phone_number,
        to=phone_number
    )    