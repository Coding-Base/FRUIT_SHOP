from django.http import HttpResponse
from django.shortcuts import render
from .models import Products,Blog

def index(request):
     product = Products.objects.all()
     blog = Blog.objects.all()
     return render(request,'index.html',{'products':product, 'blogs':blog})

 

def new(request):
     return HttpResponse('new product')
  


   




