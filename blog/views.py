from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import BlogPost
from django.urls import reverse_lazy

class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

class BlogPostCreateView(CreateView):
    model = BlogPost
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('blog:post_list')

class BlogPostUpdateView(UpdateView):
    model = BlogPost
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('blog:post_list')

class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('blog:post_list')

