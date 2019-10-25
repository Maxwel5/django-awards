from django.shortcuts import render
from .forms import PostForm
from .models import Post

# Create your views here.
def homePageView(request):
    # model = Post
    post = Post.objects.all()
    return render(request,'pages/home.html', {'post':post})

def createPostView(request):
    post = Post.objects.all()
    form = PostForm
    return render(request,'pages/post.html', {'form':form})


