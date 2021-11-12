from django.shortcuts import render
from django.views.generic import ListViews, DetailView, CreateView
from .models import Post


# def home(request):
  #  return render(request,'home.html',{})

class HomeView(ListViews):
    model = Post
    template_name = 'home.html'

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'detail.html'

class AddPostView(CreateView):
    model = Post
    template_name = 'add_post.html'
    fields = '__all__'



