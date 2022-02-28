from .models import Profile
from .serializers import ProfileSerializers
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from django.shortcuts import get_object_or_404
from rest_framework import status

class ProfileViewSet(ViewSet):

    def list(self, request):
        queryset = Profile.objects.all()
        serializer = ProfileSerializers(queryset,many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        profile = get_object_or_404(Profile, pk=pk)
        serializer = ProfileSerializers(profile)
        return Response(serializer.data, status.HTTP_200_OK)

    def partial_update(self, request, pk=None):
        profile = get_object_or_404(Profile, pk=pk)
        serializer = ProfileSerializers(profile,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

