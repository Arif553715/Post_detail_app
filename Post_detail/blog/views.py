from django.shortcuts import render
from .models import Post
# Create your views here.
def home(request):
    post_list=Post.objects.all()
    return render(request,'index.html',{'Arif':post_list})


def detail(request,post_id):
    details=Post.objects.get(pk=post_id)
    return render(request,'detail.html',{'detai':details})