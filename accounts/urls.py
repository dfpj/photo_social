from django.urls import path
from .views import CreateUser,VerifyUser

app_name ='accounts'

urlpatterns = [
    path('create/',CreateUser.as_view()),
    path('verify/',VerifyUser.as_view())
]
