from django.urls import path
from .views import Create_Post_View, List_Posts_View, Delete_Post_View, Update_Post_View, Post_details_View, List_Users_View, \
    Block_User_View, Unblock_User_View, Create_Category_View, List_Categories_View, Update_Category_View, Delete_Category_View, Category_details_View, \
        Promote_User_View, Create_ForbiddenWord_View, List_ForbiddenWords_View, Update_ForbiddenWord_View, Delete_ForbiddenWord_View, ForbiddenWord_details_View, \
            Like_Post, Dislike_Post

urlpatterns = [
    path('create-post', Create_Post_View.as_view(), name="adminuser.create_post"),
    path('list-posts', List_Posts_View.as_view(), name="adminuser.list_posts"),
    path('delete-post/<int:pk>', Delete_Post_View.as_view(), name="adminuser.delete_post"),
    path('update-post/<int:pk>', Update_Post_View.as_view(), name="adminuser.update_post"),
    path('post-details/<int:pk>', Post_details_View, name="adminuser.post_details"),
    path('create-category', Create_Category_View.as_view(), name="adminuser.create_category"),
    path('list-categories', List_Categories_View.as_view(), name="adminuser.list_categories"),
    path('delete-category/<int:pk>', Delete_Category_View.as_view(), name="adminuser.delete_category"),
    path('update-category/<int:pk>', Update_Category_View.as_view(), name="adminuser.update_category"),
    path('category-details/<int:pk>', Category_details_View.as_view(), name="adminuser.category_details"),
    path('list-users', List_Users_View.as_view(), name="adminuser.list_users"),
    path('block-user/<int:pk>', Block_User_View, name="adminuser.block_user"),
    path('unblock-user/<int:pk>', Unblock_User_View, name="adminuser.unblock_user"),
    path('promote-user/<int:pk>', Promote_User_View, name="adminuser.promote_user"),
    path('create-forbidden-word', Create_ForbiddenWord_View.as_view(), name="adminuser.create_forbidden_word"),
    path('list-forbidden-words', List_ForbiddenWords_View.as_view(), name="adminuser.list_forbidden_words"),
    path('delete-forbidden-word/<int:pk>', Delete_ForbiddenWord_View.as_view(), name="adminuser.delete_forbidden_word"),
    path('update-forbidden-word/<int:pk>', Update_ForbiddenWord_View.as_view(), name="adminuser.update_forbidden_word"),
    path('forbidden-word-details/<int:pk>', ForbiddenWord_details_View.as_view(), name="adminuser.forbidden_word_details"),
    path('like-post/<int:pk>', Like_Post, name="adminuser.like_post"),
    path('dislike-post/<int:pk>', Dislike_Post, name="adminuser.dislike_post"),
]
