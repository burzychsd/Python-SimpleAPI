from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
	# return HttpResponse('<h1>Hello World</h2>')
	my_context = {
		"my_title": "This is my title",
		"my_number": 123,
		"my_list": ['Jim', 'John', 'Elton'],
		"my_html": "<p>What's up ?</p>"
	}
	return render(request, 'home.html', my_context)