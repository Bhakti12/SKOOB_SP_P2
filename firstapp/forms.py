from django import forms
from firstapp.models import books

class BooksForm(forms.ModelForm):
	class Meta:
		model = books
		fields = ['b_name','b_category','b_author','b_user','b_price','b_edition','b_image']