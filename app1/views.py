from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def first_app1(request):
    return HttpResponse('<h1><marquee>This Is First View Of Application One</marquee></h1>')

def second_app1(request):
    return HttpResponse('<h1><marquee>This Is second View Of Application One</marquee></h1>')
