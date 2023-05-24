from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def string2(request):
    return HttpResponse('this is string2')
def htmlpage2(request):
    return render(request,'htmlpage2.html')




