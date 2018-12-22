
from django.shortcuts import render, redirect
from finalapp.models import Document,LikedUser
from django.http import HttpResponse
from django.contrib.auth import logout
import os
from django.conf import settings
from django.contrib.auth.models import User
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.
#import pathlib
def index(request,value):
    p=Document.objects.filter(category=value)
    items=[]
    listitems=[]
    page=request.GET.get('page',1)
    paginator=Paginator(p,12)
    try:
        users=paginator.page(page)
    except PageNotAnInteger:
        users=paginator.page(1)
    except EmptyPage:
        users=paginator.page(paginator.num_pages)
    context={'items':users,'users':users,'value':value}
    return render(request, 'myapp/category/index.html', context)


def user(request,value):
    p = Document.objects.filter(user=value)
    print(Document.objects.filter(user=value))
    context={'items':p}
    return render(request, 'myapp/category/user.html', context)


def countlikes(request,imageid):
    liked_photos = None
    if request.method=='GET':
        try:
            liked_photos = LikedUser.objects.filter(user=request.user.username)

        except:
            pass

        if imageid:
            likedata=Document.objects.get(image=imageid)
            if liked_photos is not None:
                liked_images_list = []
                for entry in liked_photos:
                    liked_images_list.append(entry.image)
                if likedata.image.url in liked_images_list:
                    return HttpResponse("You've already liked this photo.")

            LikedUser.objects.create(user=request.user.username, image=likedata.image.url)
            pre_likes = likedata.likes
            pre_likes += 1
            likedata.likes = pre_likes
            likedata.save()
    return HttpResponse('you have liked the image...please go back for more images')


def category(request):
    return render(request,'myapp/category/category.html')

def user_logout(request):
    logout(request)
    return redirect('finalapp:home')
