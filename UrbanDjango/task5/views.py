import os

from django.shortcuts import render

from .forms import UserRegister
from secrets import compare_digest


def sign_up_by_django(request):
    users = {
        'alex': '12312312',
        'bob': '11111111',
        'charlie': '22222222'
    }
    info = {}

    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username'].lower()
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if compare_digest(password, repeat_password) and 100 > age >= 18 and username not in users:
                info['success'] = f'Hello, {username}'
            else:
                info['errors'] = []
                if not compare_digest(password, repeat_password):
                    info['errors'].append('Пароли не совпадают')
                if age < 18:
                    info['errors'].append('Возраст должен быть не менее 18')
                if username in users:
                    info['errors'].append('Пользователь уже существует')
    else:
        form = UserRegister()
    info['form'] = form
    info['reg_type'] = 'django'

    return render(request, os.path.join('fifth_task', 'registration_page.html'), info)


def sign_up_by_html(request):
    users = {
        'alex': '12312312',
        'bob': '11111111',
        'charlie': '22222222'
    }
    info = {}

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))

        if compare_digest(password, repeat_password) and 100 > age >= 18 and username not in users:
            info['success'] = f'Hello, {username}'
        else:
            info['errors'] = []
            if not compare_digest(password, repeat_password):
                info['errors'].append('Пароли не совпадают')
            if age < 18:
                info['errors'].append('Возраст должен быть не менее 18')
            if username in users:
                info['errors'].append('Пользователь уже существует')

    return render(request, os.path.join('fifth_task', 'registration_page.html'), info)
