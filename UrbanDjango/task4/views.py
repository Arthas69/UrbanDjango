import os

from django.shortcuts import render


# Create your views here.
def platform(request):
    return render(request, os.path.join('fourth_task', 'platform.html'), {'pagename': 'Главная страница'})


def games(request):
    games = ["Assassin's Creed", "GTA V", "DOOM 3", "Atomic Heart", "Cyberpunk 2077"]
    return render(request, os.path.join('fourth_task', 'games.html'), {'pagename': 'Игры', 'games': games})


def cart(request):
    cart = []
    # cart = [
    #     {"title": "Assassin's Creed", "price": 59.99},
    #     {"title": "GTA V", "price": 59.99},
    #     {"title": "DOOM 3", "price": 59.99},
    #     {"title": "Atomic Heart", "price": 59.99},
    #     {"title": "Cyberpunk 2077", "price": 59.99}
    # ]
    pagename = "Ваша корзина пуста" if not cart else "Корзина"
    return render(request, os.path.join('fourth_task', 'cart.html'), {'pagename': pagename, 'cart': cart})
