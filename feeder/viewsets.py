"""
Django REST framework allows you to combine the logic for a set of related views in a single class,
called a ViewSet. In other frameworks you may also find conceptually similar implementations named 
something like 'Resources' or 'Controllers'.
"""

from rest_framework import viewsets
from .models import User, Credential, Feeder, Galileo
from .serializers import UserSerializer, CredentialSerializer, FeederSerializer, GalileoSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CredentialViewSet(viewsets.ModelViewSet):
    queryset = Credential.objects.all()
    serializer_class = CredentialSerializer

class FeederViewSet(viewsets.ModelViewSet):
    queryset = Feeder.objects.all()
    serializer_class = FeederSerializer

class GalileoViewSet(viewsets.ModelViewSet):
    queryset = Galileo.objects.all()
    serializer_class = GalileoSerializer