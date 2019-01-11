from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def article_list_view(request):
	articles = Article.objects.all()
	context = {
		"articles": articles,
		"link": Article.get_create_url()
	}
	return render(request, 'articles/articles_list.html', context)

def article_create_view(request):
	form = ArticleForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = ArticleForm()
		return redirect('../')

	context = {
		'form': form
	}
	return render(request, 'articles/article_create.html', context)

def article_lookup_view(request, id):
	article = get_object_or_404(Article, id=id)
	context = {
		"article": article
	}
	return render(request, 'articles/article_detail.html', context)

def article_delete_view(request, id):
	article = get_object_or_404(Article, id=id)
	if request.method == 'POST':
		article.delete()
		return redirect('../')
	context = {
		"article": article
	}
	return render(request, 'articles/article_delete.html', context)