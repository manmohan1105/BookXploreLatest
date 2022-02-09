from django.urls import path
from . import views
urlpatterns=[
    
    path('',views.index,name='index'),
    path('counter',views.counter,name='counter'),
    path('register',views.register,name='register'),
    path('login',views.loginpage,name='loginpage'),
    path('home',views.home,name='home'),
    path('logoutuser',views.logoutuser,name='logoutuser'),
    path('saved/<str:user_id>/',views.saved,name='saved'),
    path('showhistory',views.showhistory,name='showhistory'),
    path('usersavedbook',views.usersavedbook,name='usersavedbook'),
    path('deletehistory/<int:historyid>/',views.deletehistory,name='deletehistory'),
    path('deletebook/<str:bookid>/',views.deletebook,name='deletebook'),

    path('userspage',views.userspage,name='userspage'),
    path('unfollow/<str:username>/',views.unfollow,name='unfollow'),
     path('follow/<str:username>/',views.follow,name='follow'),
 
 path('addpost',views.addpost,name='addpost'),
 path('allpost',views.allpost,name='allpost'),



]