# Generated by Django 4.0.6 on 2022-07-15 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Web_blog', '0002_bloggers_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bloggers',
            name='email',
        ),
        migrations.RemoveField(
            model_name='bloggers',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='bloggers',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='bloggers',
            name='password',
        ),
        migrations.AlterField(
            model_name='bloggers',
            name='account_num',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='bloggers',
            name='phone',
            field=models.CharField(max_length=30),
        ),
    ]
