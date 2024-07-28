# price_alert/urls.py
from django.contrib import admin
from django.urls import path, include
from alerts.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('alerts/', include('alerts.urls')),
    path('', home, name='home'),
]
