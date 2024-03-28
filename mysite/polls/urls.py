# polls 폴더에 urls.py가 없어서 새로 생성
from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns = [
    path("", views.index, name="index"),

    path('cafe_menu', views.cafe_menu, name='etc'),
    path('contact', views.contact, name='contact'),
    path('order_coffee', views.order_coffee, name='coffee'),
]