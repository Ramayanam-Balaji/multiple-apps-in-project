from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def string1(request):
    return HttpResponse('first string')
def htmlpage1(request):
    return render(request,'htmlpage1.html')


