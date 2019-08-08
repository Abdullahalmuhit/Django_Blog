from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('author/<name>', views.getauthor, name="author"),
    path('article/<int:id>', views.getsingle, name="single_post"),
    path('topic/<name>', views.getTopic, name="topic"),
    path('login/', views.getLogin, name="login"),
    path('logout/', views.getlogout, name="logout"),
    path('create/', views.getcreate, name="create"),
    path('profile/', views.getprofile, name="profile"),
    path('update/<int:pid>', views.getupdate, name="update"),
    path('delete/<int:pid>', views.getdelete, name="delete"),
    path('register/', views.getregister, name="register"),
    path('topics/', views.getcategory, name="category"),
    path('create/topic', views.createtopic, name="createtopic"),
    path('deletetopic/<int:pid>', views.topicdelete, name="topicdelete"),
    path('pdf/<int:id>', views.Pdf.as_view(), name = 'pdf')
]