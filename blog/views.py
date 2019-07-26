from django.shortcuts import render, get_object_or_404,HttpResponseRedirect
from post.foms import *
from post.models import Post





def post(request):

    form= PostForm(request.POST or None   )

    if form.is_valid():
        form.save ()


    context ={


        'form':form,

    }

    return render(request,'post/sinav.html', context)


def index(request):

    posts=Post.objects.all()

    return render(request,'post/index.html',{'posts':posts})

def detail(request,id):

    post = get_object_or_404(Post ,id=id)

    context = {

    'post':post,

    }
    return render(request,'post/detail.html',context)


def Update(request,id):
    post = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=post)

    if form.is_valid():
        post= form.save()

        return HttpResponseRedirect(post.get_absolute_url())

    context ={


        'form':form,

    }

    return render(request,'post/sinav.html', context)



def Header(request):

    return render(request,'post/header.html')


def odeme(request):

    return render(request,'post/odeme.html')


def radialmenu(request):

    return render(request,'post/radialmenu.html')








