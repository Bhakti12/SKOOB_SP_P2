from django.urls import path

from . import views

urlpatterns=[
	path("",views.index, name="index"),
	path('about', views.about , name="about"),
	path('who', views.who , name="who"),
	path('seller', views.seller , name="seller"),
	path('buyer', views.buyer , name="buyer"),
	path('bookform', views.bookform , name="bookform"),
	path('register',views.register, name="register"),
	path('login',views.login, name="login"),
	path('cart', views.cart , name="cart"),
	path('contact', views.contact , name="contact"),
	path('logout', views.logout , name="logout"),
	path('purchase', views.purchase , name="purchase"),
]