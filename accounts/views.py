from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import UserCreateSerializers,UserVerifySerializers
from .models import User
from .signals import verify_code_signal


class CreateUser(APIView):
    def post(self, request):
        info = UserCreateSerializers(data=request.data)
        if info.is_valid():
            data = info.validated_data
            user = User.objects.get_or_create(username=data['username'], password=data['password'])[0]
            verify_code_signal.send(sender=self.__class__,username=user.username)
            return Response({'data': 'send verify code'}, status=status.HTTP_201_CREATED)
        return Response(info.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyUser(APIView):
    def post(self, request):
        info = UserVerifySerializers(data=request.data)
        if info.is_valid():
            data = info.validated_data
            user =get_object_or_404(User,username=data['username'])
            if data['verify_code'] == user.verify_code:
                user.is_active =True
                user.save()
                return Response({'data': 'actived user'}, status=status.HTTP_200_OK)
            return Response({'data': 'verify code is wrong'}, status=status.HTTP_406_NOT_ACCEPTABLE)
        return Response(info.errors, status=status.HTTP_400_BAD_REQUEST)