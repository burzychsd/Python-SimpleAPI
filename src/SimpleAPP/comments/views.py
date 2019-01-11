from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

from .forms import CommentForm, RawCommentForm
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

# def comment_create_view(request):
# 	form = RawCommentForm()
# 	if request.method == 'POST':
# 		form = RawCommentForm(request.POST)
# 		if form.is_valid():
# 			Comment.objects.create(**form.cleaned_data)
# 	context = {
# 		'form': form
# 	}
# 	return render(request, 'comments/comment_create.html', context)

def comments_detail_view(request):
	comments = Comment.objects.all()
	context = {
		"comments": comments
	}
	return render(request, 'comments/comment_detail.html', context)

def dynamic_lookup_view(request, id):
	# comment = get_object_or_404(Comment, id=id)
	try:
		comment = Comment.objects.get(id=id)
	except Comment.DoesNotExist:
		raise Http404
	context = {
		"comment": comment
	}
	return render(request, 'comments/comment_detail.html', context)

def comment_delete_view(request, id):
	comment = get_object_or_404(Comment, id=id)
	if request.method == 'POST':
		comment.delete()
		return redirect('../')
	context = {
		"comment": comment
	}
	return render(request, 'comments/comment_delete.html', context)

