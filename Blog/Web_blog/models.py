from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Bloggers(models.Model):
    phone = models.CharField(max_length=30)
    account_num = models.CharField(max_length=100)
    user = models.OneToOneField(User , models.CASCADE, null=True)
    author = models.ImageField(upload_to='blogger/' , blank=True)
  
    
    def __str__(self):
        return self.user.username
    
class Post(models.Model):
    text_post = models.TextField()
    title = models.CharField(max_length=100, null=True)
    post_date = models.DateTimeField(default=datetime.now, blank=True)
    creator = models.ForeignKey(Bloggers , models.DO_NOTHING)
    post_image = models.ImageField(upload_to='post/', blank=True)
    likes = models.ManyToManyField(Bloggers, related_name='like_post')
    
    def __str__(self):
            return self.title


class Comments(models.Model):
    coment_text = models.TextField(max_length=200)
    post = models.ForeignKey(Post , models.CASCADE)
    creator = models.ForeignKey(Bloggers , models.CASCADE)
  
    def __str__(self):
            return 'comment'


class Contact(models.Model):
   email = models.CharField(max_length=50) 
   phone = models.CharField(max_length=20)

   def __str__(self):
            return 'contact'

