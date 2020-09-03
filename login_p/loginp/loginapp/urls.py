from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('login/',views.login, name = 'login'),
    path('signup/', views.signup, name = 'signup'),
    path('logout/', views.logout, name = 'logout'),
    path('mypost/', views.mypost, name = 'mypost'),
    path('deletepost/', views.deletepost, name = 'deletepost'),
    path('addpost/', views.addpost, name = 'addpost'),
    path('editpost/', views.editpost, name = 'editpost'),
]
