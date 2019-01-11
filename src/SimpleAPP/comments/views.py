from django.shortcuts import render

from .models import Comment
# Create your views here.
def comments_detail_view(request):
	obj = Comment.objects.get(id=1)
	context = {
		"author": obj.author,
		"text": obj.text,
		"date": obj.date
	}
	return render(request, 'comments/comment_detail.html', context)