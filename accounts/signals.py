from django.dispatch import receiver
from django.dispatch import Signal
from .models import is_email, is_mobile, User
import random

verify_code_signal = Signal()


def send_email(email, code):
    print("Email sendig ...")
    # send_mail("Photo Social",code,settings.EMAIL_HOST_USER,[email],fail_silently=False,)


def send_sms(mobile, code):
    pass


@receiver(verify_code_signal)
def send_verify_code(*args, **kwargs):
    user = User.objects.get(username=kwargs['username'])
    user.verify_code = random.randint(1000, 9999)
    user.save()
    if is_email(user.username):
        send_email(user.username, user.verify_code)
    if is_mobile(user.username):
        send_sms(user.username, user.verify_code)
