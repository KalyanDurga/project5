from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first_app2(request):
    return HttpResponse('<h1><marquee>This Is The View Of Application two <marquee><h1>')

def second_app2(request):
    return HttpResponse('<h1><marquee>This Is The View Of Application two <marquee><h1>')