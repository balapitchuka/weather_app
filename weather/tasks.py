from time import sleep

from celery import shared_task
from django.conf import settings
from django.core.mail import EmailMessage, send_mail

@shared_task
def send_weather_mail(weather_data_path, email_list):
    
    subject= 'Weather Data'
    message= 'Please find the attachment of latest weather data!'
    mail = EmailMessage(subject, message, settings.EMAIL_HOST_USER, email_list)
    mail.attach_file(weather_data_path)
    mail.send()
    return 'Mail Sent Successfully'
