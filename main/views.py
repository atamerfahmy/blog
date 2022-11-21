from django.shortcuts import render, redirect
from adminuser.models import Category, Post
# Create your views here.

def home_view(request):
    categories = Category.objects.all()
    cat_list = []
    if request.user.is_authenticated:
        for cat in categories:
            if cat.subscribed_users.contains(request.user):
                cat.is_subscribed = True
                cat_list.extend(list(cat.get_posts()))
            else:
                cat.is_subscribed = False
        posts = Post.objects.all()
    else:
        posts = Post.objects.all()
    return render(request , 'main/home.html', context={'categories': categories, "posts": posts, "cat_list": cat_list })


def subscribe_view(request, pk):
    category = Category.objects.get(pk=pk)
    category.subscribed_users.add(request.user)
    category.save()
    return redirect('home')

def unsubscribe_view(request, pk):
    category = Category.objects.get(pk=pk)
    category.subscribed_users.remove(request.user)
    category.save()
    return redirect('home')

def category_posts_view(request, id):
    posts = Post.objects.filter(category_id=id).order_by('-created_at')
    return render(request , 'main/category_posts.html', context={'posts': posts}) 