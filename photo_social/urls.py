from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from accounts.views import UserViewSet

router =routers.DefaultRouter()
router.register('accounts',UserViewSet,basename='user')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
