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


def s4_1(request):
    return render(request, 'text/s4_1.html')


def s4_2(request):
    return render(request, 'text/s4_2.html')


def s4_3(request):
    return render(request, 'text/s4_3.html')


def s4_4(request):
    return render(request, 'text/s4_4.html')


def s4_5(request):
    return render(request, 'text/s4_5.html')


def s4_6(request):
    return render(request, 'text/s4_6.html')


def s4_7(request):
    return render(request, 'text/s4_7.html')


def s4_8(request):
    return render(request, 'text/s4_8.html')


def s4_9(request):
    return render(request, 'text/s4_9.html')
