#I have created this file - Yash
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    params = {'name': 'Yash', 'place': 'India'}
    return render(request, 'index.html', params)

def about(request):
    return render(request, 'about.html')

def remove_punctuation(request):
    return render(request, 'remove-punc.html')

def capitalize(request):
    return render(request, 'capitalize.html')

def space_remover(request):
    return render(request, 'space-remover.html')

def char_count(request):
    return render(request, 'charcount.html')

def line_remover(request):
    return render(request, 'lineremover.html')