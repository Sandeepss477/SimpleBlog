from typing import Any
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView
from.models import Post,Category,Comment
from.forms import PostForm,CommentForm
from django.urls import reverse_lazy


# Create your views here.
# def home(request):
#     return render(request,'home.html',{})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView,self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

def CategoryView(request, cats):
        category_posts = Post.objects.filter(category=cats)
        return render(request, 'categories.html',{'cats':cats, 'category_posts':category_posts}) 

        

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'


       

class AddPostView(CreateView):
    model = Post 
    form_class = PostForm 
    template_name = 'add_post.html'
    # fields = '__all__'  
    # fields = ('title','author','body') 

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm 
    template_name = 'add_comment.html'
    # fields = '__all__'

    def form_valid(self, form):
         form.instance.post_id = self.kwargs['pk']
         return super().form_valid(form)
      
    success_url = reverse_lazy ('home') 

class AddCategoryView(CreateView):
    model = Category 
    # form_class = PostForm 
    template_name = 'add-category.html' 
    fields = '__all__'  

class UpdatePostView(UpdateView):
     model = Post
     template_name = 'update_post.html'
     fields = ['title','body']    

class DeletePostView(DeleteView):
     model = Post
     template_name = 'delete_post.html'
     fields = '__all__'
     success_url = reverse_lazy('home') 


