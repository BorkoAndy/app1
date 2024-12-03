from django.contrib import auth, messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from traitlets import Instance
from django.contrib.auth.decorators import login_required

from users.forms import UserLoginForm, UserProfileForm, UserRegistrationForm

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
                messages.success(request, "Succesfully logged")

                if request.POST.get('next', None):
                    return HttpResponseRedirect(request.POST.get('next'))
                
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()

    context = {   
        'form': form     
    }    
    return render (request, 'users/login.html', context)

@login_required
def logout(request):
    auth.logout(request) 
    messages.success(request, "Succesfully logged out")    
    return redirect(reverse('main:index'))


def registration(request):
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():            
            form.save()
            user = form.instance
            auth.login(request, user)
            messages.success(request, "Succesfully registered and logged in")
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegistrationForm()

    context = {  
        'form': form      
    }    
    return render (request, 'users/registration.html', context)

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
    }    
    return render (request, 'users/profile.html', context)


def users_cart(request): 
    return render (request, 'users/users_cart.html')


