from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
def home_page(request):
    return render(request, 'platform.html')


def game_page(request):
    return render(request, 'games.html')


def cart_page(request):
    return render(request, 'cart.html')
