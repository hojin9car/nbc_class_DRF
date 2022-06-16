from rest_framework.renderers import serializers
from .models import Article as ArticleModel


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleModel
        fields = ['title', 'content', 'author_id']
