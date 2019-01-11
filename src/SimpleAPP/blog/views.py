from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
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

class ArticleUpdateView(View):
	template_name = 'articles/article_update.html'
	def get_object(self):
		id = self.kwargs.get('id')
		obj = None
		if id is not None:
			obj = get_object_or_404(Article, id=id)
		return obj

	def get(self, request, id=None, *args, **kwargs):
		context = {}
		obj = self.get_object()
		if obj is not None:
			form = ArticleForm(instance=obj)
			context['object'] = obj
			context['form'] = form
		return render(request, self.template_name, context)

	def post(self, request, id=None, *args, **kwargs):
		context = {}
		obj = self.get_object()
		if obj is not None:
			form = ArticleForm(request.POST, instance=obj)
			if form.is_valid():
				form.save()
				return redirect('../')
			context['object'] = obj
			context['form'] = form
		return render(request, self.template_name, context)

