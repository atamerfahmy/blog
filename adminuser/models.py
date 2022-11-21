from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="images/posts/")
    # created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    # comments = models.ForeignKey("Author", on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name="post_likes", null=True, blank=True)
    dislikes = models.ManyToManyField(User, related_name="post_dislikes", null=True, blank=True)

    def get_image_url(self):
        return "/media/" + str(self.image)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=50)
    subscribed_users = models.ManyToManyField(User, related_name="subscribed_users", null=True, blank=True)

    def get_posts(self):
        return Post.objects.filter(category=self)

    def __str__(self):
        return self.name


class Comment(models.Model):
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    content = models.CharField(max_length=200)
    reply = models.ForeignKey("Comment", on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return str(self.id)


class ForbiddenWords(models.Model):
    word = models.CharField(max_length=50)

    def __str__(self):
        return self.word
    