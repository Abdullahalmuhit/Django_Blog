from django.urls import path
from .views import ArticleAPIView, AuthorAPIView, CategoryAPIView, CommentAPIView, ArticleAPIDetailsView, ArticleAPINewView
from .views import CategoryAPIDetailsView, CategoryAPINewView, AuthorAPIDetailsView, AuthorAPINewView, CommentAPIDetailsView, CommentAPINewView

urlpatterns = [
    path('', ArticleAPIView.as_view()),
    path('author_api/', AuthorAPIView.as_view()),
    path('category_api/', CategoryAPIView.as_view()),
    path('comment_api/', CommentAPIView.as_view()),

    #  api_crud

    path('article_details/<int:pk>/', ArticleAPIDetailsView.as_view()),
    path('article_details/new', ArticleAPINewView.as_view()),

    path('category_details/<int:pk>/', CategoryAPIDetailsView.as_view()),
    path('category_details/new', CategoryAPINewView.as_view()),

    path('author_details/<int:pk>/', AuthorAPIDetailsView.as_view()),
    path('author_details/new', AuthorAPINewView.as_view()),


    path('comment_details/<int:pk>/', CommentAPIDetailsView.as_view()),
    path('comment_details/new', CommentAPINewView.as_view()),


]