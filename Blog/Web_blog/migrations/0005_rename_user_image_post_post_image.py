# Generated by Django 4.0.6 on 2022-07-15 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Web_blog', '0004_post_title_post_user_image_alter_post_text_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='user_image',
            new_name='post_image',
        ),
    ]
