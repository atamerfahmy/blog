# Generated by Django 4.1.3 on 2022-11-21 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminuser', '0004_forbiddenwords_comment_created_at_comment_post'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]