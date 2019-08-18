from django.shortcuts import render
from blogapp.models import author, article, comment, category
from rest_framework import generics, permissions
from .serializers import ArticleSerializer, AuthorSerializer, CategorySerializer, CommentSerializer

# article api view
class ArticleAPIView(generics.ListAPIView):
    queryset = article.objects.all()
    serializer_class = ArticleSerializer

#author api view
class AuthorAPIView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = author.objects.all()
    serializer_class = AuthorSerializer

# category api view
class CategoryAPIView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = category.objects.all()
    serializer_class = CategorySerializer


class CommentAPIView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = comment.objects.all()
    serializer_class = CommentSerializer


# article details view

class ArticleAPIDetailsView(generics.RetrieveUpdateDestroyAPIView):  # for update delete
    permission_classes = (permissions.IsAuthenticated,)
    queryset = article.objects.all()
    serializer_class = ArticleSerializer

class ArticleAPINewView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = article.objects.all().order_by('-id')[:1]
    serializer_class = ArticleSerializer


# category details view

class CategoryAPIDetailsView(generics.RetrieveUpdateDestroyAPIView): # for update delete
    permission_classes = (permissions.IsAuthenticated,)
    queryset = category.objects.all()
    serializer_class = CategorySerializer

class CategoryAPINewView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = category.objects.all().order_by('-id')[:1]
    serializer_class = CategorySerializer



# author details view

class AuthorAPIDetailsView(generics.RetrieveUpdateDestroyAPIView): # for update delete
    queryset = author.objects.all()
    serializer_class = AuthorSerializer

class AuthorAPINewView(generics.ListCreateAPIView):
    queryset = author.objects.all().order_by('-id')[:1]
    serializer_class = AuthorSerializer


# comment details view

class CommentAPIDetailsView(generics.RetrieveUpdateDestroyAPIView): # for update delete
    queryset = comment.objects.all()
    serializer_class = CommentSerializer

class CommentAPINewView(generics.ListCreateAPIView):
    queryset = comment.objects.all().order_by('-id')[:1]
    serializer_class = CommentSerializer