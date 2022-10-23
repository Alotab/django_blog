from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post

# Create your views here.


def home(request):
    context = { 
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)





class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']




class UserPostListView(ListView):
    model = Post
    template_name = 'blog/home.html'



    





class PostDetailView(DetailView):
    model = Post