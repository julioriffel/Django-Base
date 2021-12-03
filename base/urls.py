#  Copyright (c) 2021.
#  Julio Cezar Riffel<julioriffel@gmail.com>
from django.urls import path

from base import views

urlpatterns = [
    path('a', views.a, name='a'),
]
