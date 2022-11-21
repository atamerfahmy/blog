# Generated by Django 4.1.3 on 2022-11-21 19:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('adminuser', '0013_alter_post_dislikes_alter_post_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='subscribed_users',
            field=models.ManyToManyField(blank=True, null=True, related_name='subscribed_users', to=settings.AUTH_USER_MODEL),
        ),
    ]
