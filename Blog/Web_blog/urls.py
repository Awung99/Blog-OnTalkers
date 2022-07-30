from unicodedata import name
from django.urls import path
from Web_blog import views
from django.contrib.auth.views import LoginView

urlpatterns = [ 
    path('',views.home, name= 'home'),
    path('login',views.loginUser, name= 'login'),
    path('register',views.register, name= 'register'),
    path('form' ,views.form, name= 'form'),
    path('logout' , views.logoutUser, name='logout' ),
    path('about/' , views.about, name='about'),
    path('center/' , views.center, name='center'),
    path('post_comment/<id>', views.comments, name='comments'),
    path('post_like/<id>', views.likes, name='likes'),
    path('contact/', views.contact, name= 'contact'),
    path('detailpage/<id>', views.detailpages, name='detailpages'),
    path('profile/<id>',views.profile, name='profile' ),
    path('allpost/' ,views.allpost, name= 'allpost'),
    
]


  




