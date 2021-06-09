from django.db import models

# Create your models here.
class Books(models.Model):
	b_name = models.CharField(max_length=100)
	b_category = models.CharField(max_length=100)
	b_author = models.CharField(max_length=100)
	b_user = models.CharField(max_length=100)
	b_price = models.IntegerField()
	b_edition = models.CharField(max_length=100)
	b_image = models.ImageField(upload_to='images' , default='asdfghjkl')

class Cart(models.Model):
	b_id = models.IntegerField(max_length=20)
	b_name = models.CharField(max_length=100)
	b_price = models.IntegerField(max_length=20)
	total_cost = models.IntegerField(max_length=20)

class Category(models.Model):
	c_name = models.CharField(max_length=100)

class Users(models.Model):
	u_name = models.CharField(max_length=100)
	u_email = models.CharField(max_length=100)
	u_pass = models.CharField(max_length=100)
	u_add = models.CharField(max_length=100)
	u_city = models.CharField(max_length=100)
	u_contact = models.IntegerField(max_length=12)
	u_book = models.CharField(max_length=100)



class Admin(models.Model):
	a_name = models.CharField(max_length=100)
	a_email = models.CharField(max_length=100)
	a_password = models.CharField(max_length=100)