
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.views.static import serve
from app.user import views

urlpatterns = [
    path("test", views.test)
]
