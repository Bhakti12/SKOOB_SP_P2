from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static


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
	path('purchase', views.complete_order , name="purchase"),
	path('search', views.search , name="search"),
	path('Home_seller', views.Home_seller , name="Home_seller"),
	path('Home_buyer', views.Home_Buyer , name="Home_Buyer"),
	path('add_book', views.bookform , name="add_book"),
	path('delete_book/<id>', views.delete_view , name="delete_book"),
	#path('edit-book/<id>', views.edit_view , name="edit-book"),
	path('seller', views.storebook, name="seller"),	
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)