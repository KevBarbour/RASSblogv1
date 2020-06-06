from django.views import generic
from .models import Post
from django.shortcuts import render
from django.views.generic import TemplateView


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 3


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


class AboutPageView(generic.TemplateView):
    template_name = "about.html"


class ProjectsPageView(TemplateView):
    template_name = "projects.html"


class ContactPageView(TemplateView):
    template_name = "contact.html"


class TermsPageView(TemplateView):
    template_name = "terms.html"


class PrivacyPageView(TemplateView):
    template_name = "privacy.html"


class DisclaimerPageView(TemplateView):
    template_name = "disclaimer.html"

# Create your views here.

def index(request):
    my_dict = {"insert_me": "I am from views.py"}
    return render(request, 'index.html', context=my_dict)
