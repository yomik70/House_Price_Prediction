from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('pred_price', views.pred_price, name="pred_price")
]
