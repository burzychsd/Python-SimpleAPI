from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
	# return HttpResponse('<h1>Hello World</h2>')
	return render(request, 'home.html', {})