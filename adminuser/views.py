from django.http import HttpResponse
from adminuser.models import Category, Comment, ForbiddenWords, Post
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from django.contrib.auth.decorators import login_required

# Create your views here.
class Create_Post_View(CreateView):
    model = Post
    template_name = "adminuser/add_post.html"
    fields = [
        'title',
        'content',
        'image',
        'category'
    ]
    success_url = "/adminuser/create-post"
    success_message = 'Doc successfully created!'
    error_message = 'Error saving the Doc, check fields below.'


class List_Posts_View(ListView):
    model = Post
    template_name = "adminuser/list_posts.html"
    context_object_name = "posts"


class Update_Post_View(UpdateView):
    model = Post
    template_name = "adminuser/update_post.html"
    fields = [
        'title',
        'content',
        'image',
        'category'
    ]
    success_url = "/adminuser/list-posts"
    success_message = 'Doc successfully updated!'
    error_message = 'Error saving the Doc, check fields below.'


class Delete_Post_View(DeleteView):
    model = Post
    success_url = "/adminuser/list-posts"
    template_name = "adminuser/delete_post.html"


# class Post_details_View(DetailView):
#     model = Post
#     template_name = "adminuser/post_details.html"
#     fields = "__all__"

def Post_details_View(request, pk):
    post = Post.objects.get(pk=pk)
    is_liked = None
    is_disliked = None

    if request.user.is_authenticated:
        is_liked = post.likes.contains(request.user)
        is_disliked = post.dislikes.contains(request.user)

    if request.POST:    
        comment = Comment()

        comment.post = post
        comment.user = request.user
        
        if request.POST.get('content'):
            forbidden_words = ForbiddenWords.objects.all()
            forbidden_words_list = []

            for word in forbidden_words:
                forbidden_words_list.append(word.word)

            words = request.POST['content'].split(" ")

            new_words = []
            for word in words:
                if word in forbidden_words_list:
                    result_str = ''.join("*" for i in range(len(word)))
                    new_words.append(result_str)
                else:
                    new_words.append(word)

            comment.content = " ".join(new_words)
            
        if request.POST.get('reply'):
            comment_data = Comment.objects.get(pk=request.POST['reply'])
            comment.reply = comment_data
        comment.save()

    comments = Comment.objects.filter(post_id=pk, reply=None)

    for comment in comments:
        replies = Comment.objects.filter(reply=comment.id)
        comment.replies = replies

    return render(request, "adminuser/post_details.html", context={ "post": post, "comments": comments, "is_liked": is_liked, "is_disliked": is_disliked })


class Create_Category_View(CreateView):
    model = Category
    template_name = "adminuser/add_category.html"
    fields = ['name']
    success_url = "/adminuser/create-category"
    success_message = 'Doc successfully created!'
    error_message = 'Error saving the Doc, check fields below.'


class List_Categories_View(ListView):
    model = Category
    template_name = "adminuser/list_categories.html"
    context_object_name = "categories"


class Update_Category_View(UpdateView):
    model = Category
    template_name = "adminuser/update_category.html"
    fields = ['name']
    success_url = "/adminuser/list-categories"
    success_message = 'Doc successfully updated!'
    error_message = 'Error saving the Doc, check fields below.'


class Delete_Category_View(DeleteView):
    model = Category
    success_url = "/adminuser/list-categories"
    template_name = "adminuser/delete_category.html"


class Category_details_View(DetailView):
    model = Category
    template_name = "adminuser/category_details.html"
    fields = "__all__"


class List_Users_View(ListView):
    model = User
    template_name = "adminuser/list_users.html"
    context_object_name = "users"


def Block_User_View(request, pk):
    user = User.objects.get(pk=pk)
    user.is_active = False
    user.save()
    return redirect("adminuser.list_users")


def Unblock_User_View(request, pk):
    user = User.objects.get(pk=pk)
    user.is_active = True
    user.save()
    return redirect("adminuser.list_users")

def Promote_User_View(request, pk):
    user = User.objects.get(pk=pk)
    user.is_staff = True
    user.save()
    return redirect("adminuser.list_users")


class Create_ForbiddenWord_View(CreateView):
    model = ForbiddenWords
    template_name = "adminuser/add_forbidden_word.html"
    fields = "__all__"
    success_url = "/adminuser/create-forbidden-word"
    success_message = 'Doc successfully created!'
    error_message = 'Error saving the Doc, check fields below.'


class List_ForbiddenWords_View(ListView):
    model = ForbiddenWords
    template_name = "adminuser/list_forbidden_words.html"
    context_object_name = "forbidden_word"


class Update_ForbiddenWord_View(UpdateView):
    model = ForbiddenWords
    template_name = "adminuser/update_forbidden_word.html"
    fields = "__all__"
    success_url = "/adminuser/list-forbidden-words"
    success_message = 'Doc successfully updated!'
    error_message = 'Error saving the Doc, check fields below.'


class Delete_ForbiddenWord_View(DeleteView):
    model = ForbiddenWords
    success_url = "/adminuser/list-forbidden-words"
    template_name = "adminuser/delete_forbidden_word.html"


class ForbiddenWord_details_View(DetailView):
    model = ForbiddenWords
    template_name = "adminuser/forbidden_word_details.html"
    fields = "__all__"

@login_required
def AddComment(request, pk):
    user_id = request.user.id
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post_id=pk)
    
    return render(request, "adminuser/post_details.html", context={ "post": post, "comments": comments })


def Like_Post(request, pk):
    post = Post.objects.get(pk=pk)
    post.likes.add(request.user)

    post.save()

    return redirect(f'/post-details/{pk}')
    

def Dislike_Post(request, pk):
    post = Post.objects.get(pk=pk)
    post.dislikes.add(request.user)

    print(post.dislikes.count())
    if post.dislikes.count() == 10:
        post.delete()
        return redirect('/')
    else:
        post.save()

    return redirect(f'/post-details/{pk}')
