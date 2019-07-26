from django.shortcuts import render
from post.models import Post


def Home(request):



    return render(request,'home.html')



