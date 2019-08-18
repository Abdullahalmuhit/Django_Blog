from rest_framework import serializers
from blogapp.models import author, category, article, comment

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = article
        fields = ('__all__')


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = author
        fields = ('__all__')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = category
        fields = ('__all__')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = comment
        fields = ('__all__')