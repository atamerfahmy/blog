"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from main.views import home_view, category_posts_view, subscribe_view, unsubscribe_view
from adminuser.views import Post_details_View

urlpatterns = [
    path('', home_view, name='home'),
    path('category-posts/<int:id>', category_posts_view, name='category.posts'),
    path('subscribe/<int:pk>', subscribe_view, name='subscribe'),
    path('unsubscribe/<int:pk>', unsubscribe_view, name='unsubscribe'),
    path('post-details/<int:pk>', Post_details_View, name='post_details'),
]
