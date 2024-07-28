from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_alert_email(email, cryptocurrency, target_price, current_price):
    subject = f"Price Alert for {cryptocurrency}"
    message = f"The price for {cryptocurrency} has reached your target of {target_price}. Current price is {current_price}."
    send_mail(subject, message, 'your_email@gmail.com', [email])
