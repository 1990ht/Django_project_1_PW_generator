from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.


def home(request):
    return HttpResponse('<h1>Love Letter</h1>'
                        '<h3>For family</h3>'
                        '<h4>Hello Laila and Kate, Papy loves you both <3!</h4>')

def maus(request):
    return render(request,'generator/maus.html')



def numbers(request):
    return render(request,'generator/home.html')


def passgen(request):
    return render(request,'generator/passgen.html')


def aboutme(request):
    return render(request,'generator/aboutme.html')






def generated(request):


    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('capslock'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('numbers'):
        characters.extend(list('123456890'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()_+=-'))

    length = int(request.GET.get('length', 12))

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request,'generator/generated.html', {'password': thepassword})

