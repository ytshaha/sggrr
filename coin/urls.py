from django.urls import path
from django.conf import settings
from . import views

app_name = 'coin'

urlpatterns = [
    path('', views.coin, name='coin'),
    path('test/', views.coin2, name='coin2'),
]