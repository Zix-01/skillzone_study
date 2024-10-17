from django.urls import path

from blog.views import BlogPostCreateView, BlogPostListView, BlogPostDetailView, BlogPostDeleteView, BlogPostUpdateView

app_name = 'blog'


urlpatterns = [
    path('create/', BlogPostCreateView.as_view(), name='post_create'),
    path('', BlogPostListView.as_view(), name='post_list'),
    path('<int:pk>/view', BlogPostDetailView.as_view(), name='post_view'),
    path('<int:pk>/update', BlogPostUpdateView.as_view(), name='post_edit'),
    path('<int:pk>/delete', BlogPostDeleteView.as_view(), name='post_delete'),
]
