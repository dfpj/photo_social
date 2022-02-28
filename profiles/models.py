from accounts.models import User
from django.db import models

class Profile(models.Model):
    ITEM_GENDERS =(
        ('F','Female'),
        ('M','Male'),
        ('C','Custom')
    )
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    first_name= models.CharField(max_length=50,null=True)
    last_name= models.CharField(max_length=50,null=True)
    image = models.ImageField(default="1.jpg")
    gender = models.CharField(choices=ITEM_GENDERS,max_length=1,default='C')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'