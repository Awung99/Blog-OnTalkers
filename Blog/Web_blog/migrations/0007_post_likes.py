# Generated by Django 4.0.6 on 2022-07-21 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Web_blog', '0006_bloggers_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(related_name='blog_post', to='Web_blog.bloggers'),
        ),
    ]
