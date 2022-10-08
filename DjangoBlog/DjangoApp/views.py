from django.shortcuts import render
from .models import Blog
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login
from django.contrib  import messages
from django.http import HttpResponseRedirect
from .forms import BlogForm


# Create your views here.
def home(request):
    allblog =  Blog.objects.all()
    return render(request,'home.html',{'blog': allblog})

def  main(request,url):
    post = Blog.objects.get(url=url)
    return render(request,'fullview.html',{'post': post})


def signin(request):
   if request.user.is_authenticated:
       return HttpResponseRedirect('/dashboard') 
   else:     
    if request.method == 'POST':
       fm  =   AuthenticationForm(request=request,data=request.POST)
       if fm.is_valid():
           name = fm.cleaned_data['username']
           passw = fm.cleaned_data['password']
           user  =  authenticate(username=name,password=passw)
           if user is not None:
               login(request,user)
               return HttpResponseRedirect('/dashboard/')
           else:
               print('Login failed')
    else:
        fm = AuthenticationForm()
    context = {'fm':fm}
    return  render(request,'signin.html',context)

def dashboard(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            blog = BlogForm(request.POST)
            if blog.is_valid():
                blog.save()
                messages.success(request, 'Blog saved successfully')
        else:
            blog =  BlogForm()               
        context = {'user':request.user ,'blog':blog}
        return render(request,'dashboard.html',context)
    else:
        return HttpResponseRedirect('/signin/')