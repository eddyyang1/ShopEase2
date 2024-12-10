from django.shortcuts import render

def home(request):
    return render(request, 'base.html')

def products(request):
    return render(request, 'products.html')

def login(request):
    return render(request, 'login.html')
