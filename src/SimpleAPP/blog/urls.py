from django.urls import path
from .views import ( 
    article_list_view, 
    article_create_view,
    article_lookup_view,
    article_delete_view
)

app_name = 'blog'
urlpatterns = [
	path('', article_list_view, name='article-list'),
	path('create/', article_create_view, name='article-create'),
    path('<int:id>/', article_lookup_view, name='article-detail'),
    path('<int:id>/delete', article_delete_view, name='article-delete')
]