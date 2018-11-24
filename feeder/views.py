from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'feeder/home.html')


def about(request):
    return render(request, "feeder/about.html")
