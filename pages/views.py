from django.shortcuts import render
from django.views.generic import TemplateView
from random import randint
# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'
class AboutPageView(TemplateView):
    template_name = 'about.html'
class ContactPageView(TemplateView):
        template_name = 'contact.html'


def info(request):
    number = randint(1, 90)
    return render(request, 'info.html', {'number': number})