#I have created this file - Yash
from django.http import HttpResponse
from django.shortcuts import render
import string

punctuations = list(string.punctuation)
# print(punctuations)
def index(request):
    params = {'name': 'Yash', 'place': 'India'}
    return render(request, 'index.html', params)

def analyze(request):
    text = request.GET.get('text','default')#get the text
    # print(text)
    removepunc = request.GET.get('removepunc','off')
    # print(removepunc)
    # analyzed = text
    punctuations = list(string.punctuation)  # List of all punctuation marks

    if removepunc == 'on':
        analyzed = ''.join(char for char in text if char not in punctuations)
    else:
        analyzed = text
        
    params ={
        'purpose':'Removed Punctuation',
        'analyzedText':analyzed
    }
    return render(request, 'analyze.html',params)

# def about(request):
#     return render(request, 'about.html')

# def remove_punctuation(request):
#     text = request.GET.get('text','default')#get the text
#     return render(request, 'remove-punc.html')

# def capitalize(request):
#     return render(request, 'capitalize.html')

# def space_remover(request):
#     return render(request, 'space-remover.html')

# def char_count(request):
#     return render(request, 'charcount.html')

# def line_remover(request):
    # return render(request, 'lineremover.html')