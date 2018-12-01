from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name="about"),
    path('feederCart', views.feederCart, name="feederCart"),
    path('feederCart/<uuid:pk>', views.feederCart, name="feederCart"),
]
