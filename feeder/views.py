from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core import serializers

from rest_framework import viewsets
from .models import User, Credential, Feeder, Galileo
from .serializers import UserSerializer, CredentialSerializer, FeederSerializer, GalileoSerializer
from .forms import FeederForm


# Create your views here.
def index(request):
    feederList = serializers.serialize("json", Feeder.objects.all())
    return render(request, 'feeder/home.html', {'feederList': feederList})


def about(request):
    return render(request, "feeder/about.html")


def feederCart(request, feeder_id=None):
        return render(request, "feeder/feederCart.html", {'feeder_id', feeder_id})


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
