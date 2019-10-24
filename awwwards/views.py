from django.shortcuts import render
from .models import Post

# Create your views here.
def HomePageView(request):
    # model = Post
    post = Post.objects.all()
    return render(request,'pages/home.html')
