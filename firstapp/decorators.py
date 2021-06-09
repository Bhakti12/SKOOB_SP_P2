from django.http import HttpResponse
from django.shortcuts import redirect

#decorators is adds another function in as parameter and lets us add a little extra functionality before the original function is called so i can be added to original function using @ mark.

def requiredregister(view_func):
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('index')
		else:
			return view_func(request, *args, **kwargs)

		return view_func(request, *args, **kwargs)

	return wrapper_func

def allowed_users(allowed_roles=[]):
	def decorator(view_func):
		def wrapper_func(request, *args, **kwargs):

			print('working:', allowed_roles)
			return view_func(request, *args, **kwargs)
		return wrapper_func
	return decorator