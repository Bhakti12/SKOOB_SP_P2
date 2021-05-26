from django.db import models

# Create your models here.
class student(models.Model):
	studentt_id=models.CharField(max_length=20)
	student_name=models.CharField(max_length=20)
	student_surname=models.CharField(max_length=20)
	student_dob=models.DateTimeField()
	student_address=models.CharField(max_length=30)
	student_city=models.CharField(max_length=30)
	student_contact=models.CharField(max_length=30)
	class Meta:
		db_table = "student"