# 참고자료
# https://wisdom-990629.tistory.com/entry/DRF-APIView%EB%A1%9C-CRUD-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0

from django.shortcuts import redirect

from django.views.generic import TemplateView
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

from rest_framework.views import APIView  # method 를 커스텀 할 수 있다. def method_name():
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from .serializers import UserSerializer, LoginUserInfo
from blog.serializers import ContentSerializer

from .models import User
from blog.models import Article as ArticleModel


class Login(APIView):

    def post(self, request):
        username = request.data.get('username', '')
        password = request.data.get('password', '')

        print("username:", username)

        user = authenticate(request, username=username, password=password)
        if not user:
            return Response({"error": "존재하지 않는 계정이거나 비밀번호가 틀립니다."})
            # return redirect('login')
        print("user.id:", user.id)
        user_data = User.objects.get(username=username)
        print("---user_data====")
        print(user_data)
        data = LoginUserInfo(user_data).data
        content_data = ContentSerializer(ArticleModel.objects.filter(author_id=user.id), many=True).data
        # content_data = ArticleModel.objects.filter(author_id=user.id)
        print(content_data)
        print(type(data))
        login(request, user)
        return Response([data, content_data], status=status.HTTP_200_OK)  # 수업자료
        # return Response(template_name='blog/board.html')  # 됨. 근데 redirect 랑 둘 중에 뭘 써야할까

    def get(self, request):
        print("user get input!!")

        user_serializer = UserSerializer(User.objects.all(), many=True).data
        # print(user_serializer)
        # data = JSONRenderer().render(user_serializer)
        # print(data)
        return Response(user_serializer, status=status.HTTP_200_OK)


class Logout(APIView):

    def get(self, request):
        logout(request)

        return redirect('blog')


class SignUp(APIView):

    def post(self, request):
        username = request.data.get('username', '')
        password1 = request.data.get('password1', '')
        password2 = request.data.get('password2', '')

        if password1 != password2:
            return redirect('signup')

        user = User.objects.create_user(username=username, password=password1)

        return redirect('login')

