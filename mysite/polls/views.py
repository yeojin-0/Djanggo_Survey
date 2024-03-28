from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world")
# Create your views here.

def cafe_menu(request):
    return HttpResponse("LIKE LION 카페 메뉴에 대해 알고 싶으신가요?")

def contact(request):
    return HttpResponse("도움이 필요 하시면 말해주세요")

def order_coffee(request):
    return HttpResponse("커피 한잔 주세요")
