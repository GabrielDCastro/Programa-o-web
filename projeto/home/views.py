from django.shortcuts import render

def home(request):
    return render(request, 'home/home.html')

def contato(request):
    return render(request, 'home/contato.html')
