from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+ \
    static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)