from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hi(request):
    return render(request,'demoapp/hi.html')
    #HttpResponse('<h1>title aqui</h1>')
