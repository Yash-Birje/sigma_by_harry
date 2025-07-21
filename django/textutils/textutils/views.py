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
    fullcaps = request.GET.get('fullcaps','off')
    punctuations = list(string.punctuation)  # List of all punctuation marks
    newlineremover = request.GET.get('newlineremover','off')
    charcount = request.GET.get('charcount','off')

    if removepunc == 'on':
        analyzed = ''.join(char for char in text if char not in punctuations)
        params ={
        'purpose':'Removed Punctuation',
        'analyzedText':analyzed
    }
    elif fullcaps =='on':
        analyzed = ''.join(char.upper() for char in text)
        params ={
        'purpose':'Changed to Uppercase',
        'analyzedText':analyzed
    }
    elif newlineremover=='on':
        analyzed = ''.join(char for char in text if char!='/n')
        params ={
        'purpose':'Removed new lines(made it contiguous)',
        'analyzedText':analyzed
    }
    elif charcount=='on':
        text2 = ''.join(char for char in text if char!='/n' or char!=' ')
        analyzed = f' There are {len(text2)-13} characters in the text you gave'
        params ={
        'purpose':'Finding out number of characters in text',
        'analyzedText':analyzed
    }
    else:
        analyzed = text

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