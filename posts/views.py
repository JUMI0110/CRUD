from django.shortcuts import render
from .models import Post

# Create your views here.

def index(request):
    posts = Post.objects.all() # Post클래스의 모든 객체 가져오는 함수
    
    context = {
        'posts': posts
    }
    
    return render(request, 'index.html', context)
