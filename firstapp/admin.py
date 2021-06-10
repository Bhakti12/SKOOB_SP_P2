from django.contrib import admin

# Register your models here.
from .models import category,books

admin.site.register(category)
admin.site.register(books)