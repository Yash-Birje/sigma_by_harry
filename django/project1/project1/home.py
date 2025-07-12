from django.http import HttpResponse
content = ""
with open('C:\\Users\\yashb\\OneDrive\\Desktop\\general\\little projects\\webdev\\sigmaByHarry\\learn\\django\\project1\\project1\\one.txt', 'r') as file:
    content = file.read()
def home(request):
    return HttpResponse(content)