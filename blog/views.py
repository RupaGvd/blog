from django.shortcuts import render,HttpResponseRedirect
from .forms import UserCreationForm,AuthenticationForm,Signupform,NewPostForm
from .models import Post
from django.contrib.auth import login,logout,authenticate
# Create your views here

def home(request):
    posts = Post.objects.all()
    context = {'posts':posts,'user':request.user}
    return render(request,'blog/home.html',context)

def user_signup(request):
    if request.method=='GET':
        form = Signupform()
    else:
        form = Signupform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/login')
    context = {'form':form}
    return render(request,'blog/login.html',context)

def user_login(request):
    if request.method=='GET':
        form = AuthenticationForm()
    else:
        form = AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            uname  = form.cleaned_data['username']
            pwd = form.cleaned_data['password']
            user = authenticate(username=uname,password=pwd)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/dashboard')
    context = {'form':form}
    return render(request,'blog/login.html',context)

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
    

def dashboard(request):
    if request.user.is_authenticated:
        return render(request,'blog/dashboard.html')
    else:
        form = AuthenticationForm()
        context = {'form':form}
        return render(request,'blog/login.html',context)
    
def user_profile(request):
    if request.user.is_authenticated:
        return render(request,'blog/profile.html')
    else:
        return HttpResponseRedirect('/login')
    
def newpost(request):
    if request.method =='GET':
        form = NewPostForm()
    else:
        form = NewPostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    context = {'form':form}
    return render(request,'blog/newpost.html',context)