
from django.urls import path
from django.conf.urls import include
from . import views
urlpatterns = [
    path('homepage', views.index, name='index'),
    
    path('rider', views.rider, name='index'),

    path('provider', views.provider, name='index'),
]