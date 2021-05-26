from django import forms
from student.models import student
class studentform(forms.Modelform):
	class Meta:
		model=student
		fields="__all__"