from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models
from .models import Posts
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout 

def test(request):
    return render(request, 'blog/loginn.html')

def loginn(request):
    if request.method == "POST":
        name =  request.POST.get('uname')
        password = request.POST.get('upassword')
        userr = authenticate(request, username=name, password=password)
        if userr is not None:
            login(request, userr)
            return redirect('/home')
        else:
            return redirect('/loginn')
    return render(request, 'blog/loginn.html')

def signup(request):
    if request.method == "POST":
        name =  request.POST.get('uname')
        email = request.POST.get('uemail')
        password = request.POST.get('upassword')
        newUser = User.objects.create_user(username=name, email=email, password=password)
        newUser.save()
        return redirect('/loginn')
    return render(request, 'blog/signup.html')

def home(request):
    context = {
        'posts': Posts.objects.all().order_by('-date_posted')
    }
    return render(request, 'blog/home.html', context)

def newPost(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        npost = models.Posts(title=title, content=content, author=request.user)
        npost.save()
        return redirect('/home')
    return render(request, 'blog/newpost.html')

def myPost(request):
    context = {'posts': Posts.objects.filter(author=request.user)}
    return render(request, 'blog/mypost.html', context) 

def signOut(request):
    logout(request)
    return redirect('/loginn')
    