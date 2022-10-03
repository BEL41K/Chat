from django.contrib.auth.decorators import login_required
from django.template.defaulttags import url
from django.urls import path, include
from . import views
from .views import *
from django.utils.translation import gettext_lazy as _


urlpatterns = [
    path('', index, name='index'),
    path('room_list/', room_list, name='room_list'),
    path('register/', Register.as_view(), name='register'),
    path('', include('django.contrib.auth.urls')),
    path('room_list/chat/', chat, name='chat')
]
