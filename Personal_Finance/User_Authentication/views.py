from django.shortcuts import render
from django.http import request,response
# Create your views here.
def home(request):
    return render(request,'homepage.html')