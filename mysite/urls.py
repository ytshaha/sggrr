from django.contrib import admin
from django.urls import path
from base.views import index
from django.conf.urls import include, url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    url(r'^lotto/', include('lotto.urls')),
]

