from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')
    #return HttpResponse('<h1>Home</h1')

def productPage(request):
    return render(request, 'product.html')
    #eturn HttpResponse('<h1>About Page</h1')
