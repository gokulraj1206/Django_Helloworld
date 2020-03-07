from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView, UpdateView, DeleteView
from .models import Post
"""
posts = [
    {
        'author':'Gokul',
        'title':'Blog Post 1',
        'content':'First post content',
        'date_posted':'March 5,2020'
    },
    {
        'author':'Gopi',
        'title':'Blog Post 2',
        'content':'Second post content',
        'date_posted':'March 6,2020'
    }
]
"""
def home(request):
    context ={
        'posts':Post.objects.all()
    }
    return render(request,'blog/home.html',context)

class PostListView(ListView):
    model = Post
    template_name =  'blog/home.html'
    context_object_name ='posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post
    #default template_name for django <app>/<model>_<viewtype>.html
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



def about(request):
    return render(request,'blog/about.html',{'title': 'About'})

