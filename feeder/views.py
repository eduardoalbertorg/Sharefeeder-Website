from django.shortcuts import render
from rest_framework import viewsets
from .models import User, Credential, Feeder, Galileo
from .serializers import UserSerializer, CredentialSerializer, FeederSerializer, GalileoSerializer

# Create your views here.
def index(request):
    return render(request, 'feeder/home.html')


def about(request):
    return render(request, "feeder/about.html")


def sign(request):
    return render(request, "feeder/sign.html")


def feederCart(request):
    return render(request, "feeder/feederCart.html")

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