from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sayHello(request):
    return HttpResponse('''<h1>
                                Hello Django
                                <br>
                           </h1>
                           <sapn>
                                Hello World
                                <br> 
                                Hello World
                                <br>
                                Hello World
                           </span>''')
def hello1(request, username):
    return HttpResponse('<h1>Hello</h1>' + username)                           