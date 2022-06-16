from django.shortcuts import render, redirect

from .models import Article

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from .permissions import SignUpMoreThanMinute
from .serializers import ContentSerializer


class ReadBlog(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        collections = Article.objects.all()
        article = [data for data in collections.values()]
        print(article)
        data = Article.objects.filter(author_id=9)
        print('--------')
        print(data)
        return render(request, 'blog/board.html', {"article": article})


class Write(APIView):
    # permission_classes = [IsAuthenticated]
    permission_classes = [SignUpMoreThanMinute]

    def post(self, request):
        title = request.data.get('drf-title')
        content = request.data.get('drf-content')

        new_article = Article.objects.create(
            title=title,
            content=content,
            author_id=request.user.id
        )
        new_article.save()

        return redirect('blog')


