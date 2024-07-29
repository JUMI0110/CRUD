from django.shortcuts import render, redirect
from .models import Post

# Create your views here.

def index(request):
    posts = Post.objects.all() # Post클래스의 모든 객체 가져오는 함수
    
    context = {
        'posts': posts
    }
    
    return render(request, 'index.html', context)

def detail(request, id):
    post = Post.objects.get(id=id) # get(컬럼명=value)

    context = {
        'post': post
    }

    return render(request, 'detail.html', context)


def new(request):
    return render(request, 'new.html')

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')

    post = Post()
    post.title = title
    post.content = content
    post.save()

    # 만들어놓은 기능 재사용 redirect 
    return redirect(f'/posts/{post.id}/')
