from django.urls import path

from . import views

urlpatterns=[
	path("",views.index, name="index"),
	path('about', views.about , name="about"),
	path('who', views.who , name="who"),
	path('seller', views.seller , name="seller"),
	path('buyer', views.buyer , name="buyer"),
	
	path('register',views.register, name="register"),
	path('login',views.login, name="login"),
	path('cart', views.cart , name="cart"),
	path('contact', views.contact , name="contact"),
	path('logout', views.logout , name="logout"),
	#path('purchase', views.purchase , name="purchase"),
	path('search', views.Search , name="search"),
	path('Home_seller', views.Home_seller , name="Home_seller"),
	path('Home_buyer', views.Home_Buyer , name="Home_Buyer"),
	path('add_book', views.bookform , name="add_book"),
	#path('delete-book/<int:id>', views.deleteBook , name="delete-book"),
	#path('edit-book<int:id>', views.editBook , name="edit-book"),
	path('storebook', views.storebook, name="storebook"),	
]