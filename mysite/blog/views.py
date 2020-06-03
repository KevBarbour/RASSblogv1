from django.views import generic
from .models import Post
from django.shortcuts import render

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 3

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

# Create your views here.

def index(request):
    my_dict = {"insert_me": "I am from views.py"}
    return render(request,'index.html',context=my_dict)