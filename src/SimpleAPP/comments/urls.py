from django.urls import path
from .views import ( 
    comments_detail_view, 
    comment_create_view,
    dynamic_lookup_view,
    comment_delete_view
)

app_name = 'comments'
urlpatterns = [
	path('', comments_detail_view, name='comments-list'),
	path('create/', comment_create_view, name='comment-create'),
    path('<int:id>/', dynamic_lookup_view, name='comment-detail'),
    path('<int:id>/delete', comment_delete_view, name='comment-delete')
]