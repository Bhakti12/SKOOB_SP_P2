from django.shortcuts import render,redirect
from student.forms import studentform
from student.models import student

# Create your views here.
def std(request):
	if request.method == "POST":
		form = studentform(request.POST)
		if form.is_valid():
			try:
				form.save()
				return redirect('/show')
			except:
				pass
	else:
		form = studentform()
	return render(request,'index.html',{'form':form})
def show(request):
	students=student.objects.all()
	return render(request,"show.html",{'students':students})
def edit(request,id):
	students=student.objects.get(id=id)
	return render(request.'edit.html',{'students':students})
def update(request,id):
	students=student.objects.get(id=id)
	form=sudentform(request.POST,instance=students)
	if form.is_valid():
		form.save()
		return redirect("/show")
	return render(request,'edit.html',{'students':students})
def destroy(request,id):
	students=student.objects.get(id=id)
	students.delete()
	return redirect("/show")
	