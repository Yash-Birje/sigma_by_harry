from django.http import HttpResponse

def view(request):
    return HttpResponse(''' 
<!DOCTYPE html>
<html>
<head>
    <title>Home</title>
</head>
<body>
    <h1>Welcome to the Home Page</h1>
        <h2>This has collection of some links</h2>
    <ul>
        <li><a href="https://www.youtube.com/">Youtube</a></li>
        <li><a href="https://www.google.com/">Google</a></li>
        <li><a href="https://www.facebook.com/">Facebook</a></li>    
        <li><a href="https://www.X.com/">Twitter</a></li>
    </ul>
    <p>Enjoy exploring!</p>
</body>
</html>
    ''')