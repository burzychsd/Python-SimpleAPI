from django.shortcuts import render

from .forms import CommentForm
from .models import Comment

# Create your views here.
def comment_create_view(request):
	form = CommentForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = CommentForm()
	context = {
		'form': form
	}
	return render(request, 'comments/comment_create.html', context)

def comments_detail_view(request):
	comments = Comment.objects.all()
	context = {
		"comments": comments
	}
	return render(request, 'comments/comment_detail.html', context)