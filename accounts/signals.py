from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import is_email, is_mobile
from django.core.mail import send_mail
from django.conf import settings


def send_email(email,code):
    send_mail("Photo Social",code,settings.EMAIL_HOST_USER,[email],fail_silently=False,)

def send_sms(mobile,code):
    pass


@receiver(post_save, sender='accounts.User')
def tasks_after_save_user(sender, instance, created, *args, **kwargs):
    username = instance.username
    if created:
        if is_email(username):
            send_email(username,instance.verify_code)
        if is_mobile(username):
            send_sms(username,instance.verify_code)

