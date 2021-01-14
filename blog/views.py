from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.forms import UserCreationForm


# ---writing the views---
def home(request):
    posts = Post.objects.all()
    data = {
            'posts': posts
        }
    return render(request, 'blog/index.html', data)


def about(request):
    return render(request, 'blog/about.html')


def contact(request):
    return render(request, 'blog/contact.html')


def post(request):
    return render(request, 'blog/post.html')


def login(request):
    return render(request, 'blog/login.html')


def register(request):
    form = UserCreationForm()
    return render(request, 'blog/register.html', {'form': form})
