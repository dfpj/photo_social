from django.dispatch import receiver
from django.dispatch import Signal
from django.db.models.signals import post_save
from .models import is_email, is_mobile, User, Profile
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

@receiver(post_save,sender='accounts.User')
def create_profile(instance,created,*args, **kwargs):
    if instance.is_active:
        Profile.objects.get_or_create(user=instance)