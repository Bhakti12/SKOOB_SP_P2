from django.contrib import admin

# Register your models here.
from .models import category,books,bookorder,cart,users

admin.site.register(category)
admin.site.register(books)
admin.site.register(bookorder)
admin.site.register(cart)
admin.site.register(users)