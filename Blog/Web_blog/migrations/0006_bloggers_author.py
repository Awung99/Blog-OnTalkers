# Generated by Django 4.0.6 on 2022-07-19 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Web_blog', '0005_rename_user_image_post_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloggers',
            name='author',
            field=models.ImageField(blank=True, upload_to='post/'),
        ),
    ]
