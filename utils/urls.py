from django.contrib import admin
from django.urls import path
from  utils import views

urlpatterns = [
    path("",views.index,name="index"),
    path("analyze",views.analyze,name="analyze"),
]