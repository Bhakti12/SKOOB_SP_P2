from django.shortcuts import render,redirect
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib import messages
from django.contrib.auth.models import User,auth
from firstapp.models import Books,Cart,Category,Admin,Users
from django.contrib.auth.decorators import login_required
from .decorators import requiredregister,allowed_users
# Create your views here.
def index(request):
    return render(request, "index.html")

def register(request):
    if request.method=='POST':
        username=request.POST.get('username')
        address=request.POST.get('address')
        city=request.POST.get('city')
        contact=request.POST.get('contact')
        email=request.POST.get('email')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        
        user=User.objects.create_user(username=username,password=password,email=email)
        user.save()
        print("user created")
        return redirect('login')
    else:
        return render(request, 'register.html')

@requiredregister
@allowed_users(allowed_roles=['admin','buyer','seller'])
def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return render(request, 'who.html')
        else:
            messages.info(request, 'invalid creditionals')
            return redirect('login')
    else:
        return render(request, 'login.html')

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['buyer','seller'])
def who(request):
    return render(request, 'who.html')

def contact(request):
    return render(request, 'contact.html')

@login_required(login_url='login')
def buyer(request):
    return render(request, 'buyer.html')

@login_required(login_url='login')
def seller(request):
    return render(request, 'seller.html')

@login_required(login_url='login')
def Home_Buyer(request):
    return render(request, 'Home_Buyer.html')

@login_required(login_url='login')
def Home_seller(request):
    return render(request, 'Home_seller.html')

@login_required(login_url='login')
def purchase(request):
    return render(request, 'purchase.html')

@login_required(login_url='login')
def cart(request):
    return render(request, 'cart.html')

@login_required(login_url='login')
def profile(request):
    return render(request, 'profile.html')

@login_required(login_url='login')
def bookform(request):
    return render(request, 'bookform.html')