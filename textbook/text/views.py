from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'text/index.html')


def s1(request):
    return render(request, 'text/s1.html')


def s2(request):
    return render(request, 'text/s2.html')


def s3(request):
    return render(request, 'text/s3.html')


def s4(request):
    return render(request, 'text/s4.html')
