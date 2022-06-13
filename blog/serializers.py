from rest_framework.renderers import serializers
from .models import Article


class ContentSerializer(serializers.Serializer):

    Article.id = serializers.CharField()
    Article.title = serializers.CharField()
    Article.content = serializers.CharField()
    Article.author_id = serializers.CharField()

