from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from posts.models import Post


def post_create(request):
    return HttpResponse("<h1>Create</h1>")

def post_detail(request, id):
    #instance = Post.objects.get(id=1)
    instance = get_object_or_404(Post, id=id)
    context = {
        "instance": instance,
    }
    return render(request,"detail.html", context)

def post_list(request):
    queryset = Post.objects.all()
    context = {
        "object_list": queryset,
        "title": "List"
    }
    return render(request, "posts.html", context)

def post_update(request):
    return HttpResponse("<h1>Update</h1>")

def post_delete(request):
    return HttpResponse("<h1>Delete</h1>")
