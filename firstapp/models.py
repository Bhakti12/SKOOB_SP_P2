from django.db import models
from django.contrib.auth.models import User
from django.db.utils import OperationalError

# Create your models here.
class books(models.Model):
	b_name = models.CharField(max_length=100)
	b_category = models.CharField(max_length=100)
	b_author = models.CharField(max_length=100)
	b_user = models.CharField(max_length=100)
	b_price = models.IntegerField()
	b_edition = models.CharField(max_length=100)
	b_image = models.ImageField(upload_to='images' , default=False)
	class Meta:
		db_table="books"

class cart(models.Model):
	b_id = models.IntegerField(max_length=20)
	b_name = models.CharField(max_length=100)
	b_price = models.IntegerField(max_length=20)
	user = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
	order_date = models.DateField(null=True)
	total_cost = models.IntegerField(max_length=20)
	class Meta:
		db_table="cart"

class bookorder(models.Model):
    book = models.ForeignKey(books,on_delete=models.CASCADE)
    cart = models.ForeignKey(cart,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    class Meta:
    	db_table="bookorder"

class category(models.Model):
	c_name = models.CharField(max_length=100)
	class Meta:
		db_table="category"
	def __str__(self):
		return self.c_name

class users(models.Model):
	u_name = models.CharField(max_length=100)
	u_email = models.CharField(max_length=100)
	u_pass = models.CharField(max_length=100)
	u_add = models.CharField(max_length=100)
	u_city = models.CharField(max_length=100)
	u_contact = models.IntegerField(max_length=12)
	u_book = models.CharField(max_length=100)
	class Meta:
		db_table="users"

class admin(models.Model):
	a_name = models.CharField(max_length=100)
	a_email = models.CharField(max_length=100)
	a_password = models.CharField(max_length=100)
	class Meta:
		db_table="admin"