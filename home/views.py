from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class Home(TemplateView):
    template_name = 'index.html'

class BOD(TemplateView):
    template_name = 'bod.html'
    
