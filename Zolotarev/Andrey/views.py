from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def page(request, name, surname, age, interests):
    page = f'<h1> Me: {name} {surname}</h1>' \
        f'<p> I am {age} </p>' \
        f'<p> I like {interests} </p>'
    return HttpResponse(page)


