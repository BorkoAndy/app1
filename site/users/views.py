from django.contrib import auth, messages
from django.db.models import Prefetch
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from traitlets import Instance
from django.contrib.auth.decorators import login_required

from orders.models import Order, OrderItem
from users.forms import UserLoginForm, UserProfileForm, UserRegistrationForm
from cart.models import Cart
# Create your views here.

def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            
            session_key= request.session.session_key

            if user:
                auth.login(request, user)
                messages.success(request, "Succesfully logged")

                if session_key:
                    Cart.objects.filter(session_key=session_key).update(user=user)
                
                redirect_page = request.POST.get('next', None)
                if redirect_page and redirect_page != reverse('user:logout'):
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

            session_key= request.session.session_key

            form.save()
            user = form.instance
            auth.login(request, user)

            if session_key:
                    Cart.objects.filter(session_key=session_key).update(user=user)

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
    
    orders = (
        Order.objects.filter(user=request.user)
        .prefetch_related(
            Prefetch(
                "orderitem_set",
                queryset=OrderItem.objects.select_related('product'),
            )
        )
        .order_by("-id")
    )

    context = { 
        'form': form,
        'orders': orders       
    }    
    return render (request, 'users/profile.html', context)


def users_cart(request): 
    return render (request, 'users/users_cart.html')


