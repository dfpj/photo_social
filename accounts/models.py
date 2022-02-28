from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.core.exceptions import ValidationError
import re


def is_email(value):
    regex_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.fullmatch(regex_email, value):
        return True
    return False


def is_mobile(value):
    regex_mobile = r'^\+[1-9]{1}[0-9]{3,14}$'
    if re.fullmatch(regex_mobile, value):
        return True
    return False


class UserManager(BaseUserManager):

    def create_user(self, username, password=None):
        if not username:
            raise ValueError("Users must have an email address or a phone number")
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None):
        user = self.create_user(username=username, password=password)
        user.is_active = True
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField(max_length=100, unique=True)
    verify_code = models.PositiveSmallIntegerField(null=True)
    is_active = models.BooleanField(default=False)  # need to verify
    is_admin = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'username'

    def clean(self):
        if not is_mobile(self.username) and not is_email(self.username):
            return ValidationError("Enter Email or Phone")

    def __str__(self):
        return f"{self.username}"

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

