import os

from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = os.path.join('second_task', 'class_template.html')


def function_view(request):
    return render(request, os.path.join('second_task', 'func_template.html'))
