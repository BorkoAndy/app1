<<<<<<< HEAD
from django.contrib import auth, messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from traitlets import Instance
from django.contrib.auth.decorators import login_required

from users.forms import UserLoginForm, UserProfileForm, UserRegistrationForm
=======
from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from users.forms import UserLoginForm, UserRegistrationForm
>>>>>>> da3582c0a317addf7b9646b91452defa9e38b670

# Create your views here.

def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
<<<<<<< HEAD
                messages.success(request, "Succesfully logged")
=======
>>>>>>> da3582c0a317addf7b9646b91452defa9e38b670
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()

    context = {   
        'form': form     
    }    
    return render (request, 'users/login.html', context)
<<<<<<< HEAD
@login_required
def logout(request):
    auth.logout(request) 
    messages.success(request, "Succesfully logged out")    
=======

def logout(request):
    auth.logout(request)     
>>>>>>> da3582c0a317addf7b9646b91452defa9e38b670
    return redirect(reverse('main:index'))


def registration(request):
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():            
            form.save()
            user = form.instance
            auth.login(request, user)
<<<<<<< HEAD
            messages.success(request, "Succesfully registered and logged in")
=======
>>>>>>> da3582c0a317addf7b9646b91452defa9e38b670
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegistrationForm()

    context = {  
        'form': form      
    }    
    return render (request, 'users/registration.html', context)

<<<<<<< HEAD
@login_required
def profile(request):
    if request.method == "POST":
        form = UserProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():            
            form.save() 
            messages.success(request, "Succesfully changed")           
            return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = UserProfileForm(instance=request.user)    
    context = { 
        'form': form       
=======

def profile(request):
    context = {        
>>>>>>> da3582c0a317addf7b9646b91452defa9e38b670
    }    
    return render (request, 'users/profile.html', context)
