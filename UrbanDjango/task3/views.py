import os

from django.shortcuts import render


# Create your views here.
def platform(request):
    return render(request, os.path.join('third_task', 'platform.html'))


def games(request):
    games = ["Assassin's Creed", "GTA V", "DOOM 3"]
    return render(request, os.path.join('third_task', 'games.html'), {'games': games})


def cart(request):
    # cart = []
    cart = [{"title": "Assassin's Creed", "price": 59.99}, {"title": "GTA V", "price": 59.99}, {"title": "DOOM 3", "price": 59.99}]
    return render(request, os.path.join('third_task', 'cart.html'), {'cart': cart})
