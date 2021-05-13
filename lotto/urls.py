from django.urls import path
from django.conf import settings
from . import views

app_name = 'lotto'

urlpatterns = [
    path('', views.random_lotto, name='random_lotto'),
]