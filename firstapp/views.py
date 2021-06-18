from django.shortcuts import render,redirect
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib import messages
from django.contrib.auth.models import User,auth
from firstapp.models import books,cart,category,admin,users,bookorder
from django.contrib.auth.decorators import login_required
from .decorators import requiredregister
from django.views.generic import ListView
from firstapp.forms import BooksForm
from django.utils import timezone
from django.http import HttpResponse
from django.shortcuts import (get_object_or_404,render,HttpResponseRedirect)
from django.db.models import Q
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
#@allowed_users(allowed_roles=['admin','buyer','seller'])
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
#@allowed_users(allowed_roles=['buyer','seller'])
def who(request):
	return render(request, 'who.html')

def contact(request):
	return render(request, 'contact.html')

@login_required(login_url='login')
def buyer(request):
	book=books.objects.all()
	#for b in book
	#print b.b_name,b.b_author,b.b_category,b.b_user,b.b_price,b.b_edition,b.b_image
	context={'b':book}
	return render(request, 'buyer.html',context)
	#return render(request, 'buyer.html')

@login_required(login_url='login')
def Home_Buyer(request):
	return render(request, 'Home_Buyer.html')


@login_required(login_url='login')
def profile(request):
	return render(request, 'profile.html')

#book adding process
def bookform(request):
	if request.method == "POST":
		form = BooksForm(request.POST)  
		if form.is_valid():  
			try:  
				form.save()  
				return redirect('seller') 
				#response.user.book.create(name=n) 
			except:  
				pass  
	else:  
		form = BooksForm()
		
	return render(request, 'add_book.html',{'form':form})

def storebook(request):
	if request.method == 'POST':
		book=books()
		book.b_name=request.POST['b_name']
		book.b_category=request.POST['b_category']
		book.b_author=request.POST['b_author']
		book.b_price=request.POST['b_price']
		book.b_edition=request.POST['b_edition']
		book.b_image=request.POST['b_image']
		book.save()
	return render(request,'seller.html')

@login_required(login_url='login')
def seller(request):
	book=books.objects.all()
	#for b in book
	#print b.b_name,b.b_author,b.b_category,b.b_user,b.b_price,b.b_edition,b.b_image
	context={'b':book}
	return render(request, 'seller.html',context)

#@login_required(login_url='login')
#def edit_view(request):
#    context ={}
  
	# fetch the object related to passed id
#    book = get_object_or_404(books, id = id)
  
	# pass the object as instance in form
#    form = BooksForm(request.POST, instance = book)
  
	# save the data from the form and
	# redirect to detail_view
#    if form.is_valid():
#        form.save()
#        return HttpResponseRedirect("seller")
  
	# add form dictionary to context
#    context["form"] = form
#    return render(request, 'edit-book.html' ,context)

@login_required(login_url='login')
def delete_view(request, id):
	context ={}
	book = get_object_or_404(books, id = id)
	if request.method =="POST":
		# delete object
		book.delete()
		# after deleting redirect to 
		# home page
		return HttpResponseRedirect("/")
	return render(request, 'delete_book.html',context)


def category_list(request):
	category = None
	categories = category.objects.all()
	return render(request, 'bookform.html',{'category':category})
	
@login_required(login_url='login')
def Home_seller(request):
	return render(request, 'Home_seller')

@login_required(login_url='login')
def search(request):
	results=[]
	if request.method=="GET":
		query=request.GET.get('search')
		if query=='':
			query='None'
		results=books.objects.filter(Q(b_name__icontains=query) | Q(b_author__icontains=query))
	return render(request, 'search.html', {'query':query, 'results':results})
	#results=[]
	#if request.method=="GET":
    #	query=request.GET.get('search')
    #	if query=='':
    #		query='None'
	#	results=books.objects.filter(Q(b_name__icontains=query) | Q(b_author__icontains=query))
	#return render(request, 'search.html', {'query': query, 'results': results})

def cart(request):
	return render(request, 'cart.html')

#def add_to_cart(request, id):
#    if request.user.is_authenticated():
#        try:
#            book = books.objects.get(pk=id)
#        except ObjectDoesNotExist:
#            pass
#        else:
#            try:
#                cart = cart.objects.get(user=request.user)
#            except ObjectDoesNotExist:
#                cart = cart.objects.create(
#                    user = request.user
#                )
#                cart.save()
#            cart.add_to_cart(id)
#        return redirect('buyer')
#    else:
#        return redirect('index')


#def remove_from_cart(request, id):
#    if request.user.is_authenticated():
#        try:
#            book = books.objects.get(pk=id)
#        except ObjectDoesNotExist:
#            pass
#        else:
 #           cart = cart.objects.get(user=request.user)
 #           cart.remove_from_cart(id)
 #       return redirect('cart')
 #   else:
 #       return redirect('buyer')


def complete_order(request):
	message= "Success! Your order has been completed"
	context = {'message': message}
	return render (request, 'purchase.html',context)
	


