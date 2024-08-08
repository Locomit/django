from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html')

def fpage(request):
    return render(request,'fpage.html')