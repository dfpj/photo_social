from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .serializers import UserSerializer
from .models import User
from .signals import verify_code_signal




class UserViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = User.objects.filter(is_active=True)
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data,status.HTTP_200_OK)

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            verify_code_signal.send(sender=self.__class__, username=serializer.validated_data['username'])
            return Response(serializer.data,status.HTTP_201_CREATED)
        return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        user = get_object_or_404(User,pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = get_object_or_404(User, pk=pk)
            if serializer.validated_data['verify_code'] == user.verify_code:
                user.is_active=True
                user.save()
                return Response({"data":"success"}, status.HTTP_202_ACCEPTED)
            return Response({"data": "wrong"}, status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

