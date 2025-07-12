#I have created this file - Yash
from django.http import HttpResponse
def index(request):
    return HttpResponse("Hello, world. You're at the textutils index.")

def about(request):
    return HttpResponse("This is the about page for the textutils app.")