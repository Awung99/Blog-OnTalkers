from datetime import datetime
from xml.etree.ElementTree import Comment
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

from .models import Comments,  Post, Bloggers

def loginUser(request):
    if request.method == "POST":
        username = request.POST["username"]
        
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
            ...
        else:
            # Return an 'invalid login' error message.
            ...

    return render(request,'Login.html')

def home(request):
    all_posts = Post.objects.all()
    all_bloggers = Bloggers.objects.all()
    return render(request,'index2.html', {'posts':all_posts, 'bloggers':all_bloggers})


# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['passwordRepeat']
        if password == password2:
            if User.objects.filter(username=username).exists():
               messages.error(request, 'That username is taken')
               return redirect('register')
            else:
                user = User(username=username,email=email, first_name=first_name, last_name=last_name)
                user.set_password(password)
                user.save()
                blogger = Bloggers.objects.create(phone='000000',account_num='xxxxxxx',user=user)

                return redirect('login')
    return render(request, 'Register.html')


#create your view form here.

def form(request):
    if request.method == 'POST':
        textpost = request.POST['text_post']
        post= request.POST['posttitle']
        img= request.FILES['postfile']
        posts = Post.objects.create(text_post=textpost,post_date=datetime.now(),creator=request.user.bloggers, title=post, post_image= img)
         
        return redirect('home')
    return render(request, 'post.html')
    
#creating a logout

def logoutUser(request):
    logout(request)
    return redirect('home')

#create the about page

def about(request):

    return render(request, 'about.html')

#create your help center page

def center(request):
    
    return render(request, 'center.html')

#create your comment views
#retrive data from the database
def comments(request, id):
    if request.method == "POST":
        comments= request.POST['comment']
        post_comment=Comments.objects.create(coment_text=comments,post_id=id,creator_id=request.user.bloggers.id )
        return redirect('detailpages' ,id)


def likes(request, id):
    post_to_like = Post.objects.get(id=id)
    post_to_like.likes.add(request.user.bloggers)
    return redirect('detailpages' ,id)

#create your contact views here

def contact(request):

    return render(request, 'contact.html')

#create your detailpage views
#retrive data from the database
def detailpages(request, id):
    post_details = Post.objects.get(id=id)
    
    return render(request, 'detailpage.html', {'post': post_details})

#create your profile views here
def profile(request,id):
    thisuser= User.objects.get(id=id)
    all_userpost = thisuser.bloggers.post_set.all()
    #Get the total number of likes
    total_likes=0
    for post in all_userpost:
        total_likes += post.likes.count()



    return render(request, 'profile.html',{'thisuser': thisuser, 't_likes':total_likes})

#create your allpost views here
def allpost(request ):
    blogposts=Post.objects.all()


    return render(request, 'allpost.html',{'posts': blogposts})


    
    


        
        








