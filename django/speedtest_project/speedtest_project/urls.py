from django.contrib import admin
from django.urls import path
from core import views


urlpatterns = [
    path('', views.main, name='main'),
    path('admin/', admin.site.urls),
]
