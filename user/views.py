# 참고자료
# https://wisdom-990629.tistory.com/entry/DRF-APIView%EB%A1%9C-CRUD-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0

from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.views.generic import TemplateView
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

from rest_framework.views import APIView  # method 를 커스텀 할 수 있다. def method_name():
from rest_framework.response import Response
from rest_framework import status

from .models import User


class Login(APIView):

    def post(self, request):
        username = request.data.get('username', '')
        password = request.data.get('password', '')
        print("---1---")
        print(username)
        print(password)

        user = authenticate(request, username=username, password=password)
        if not user:
            # return Response({"error": "존재하지 않는 계정이거나 비밀번호가 틀립니다."})
            return redirect('login')

        login(request, user)
        # return Response({"message": "로그인 성공"}, status=status.HTTP_200_OK)  # 수업자료
        return redirect('blog')  # <- 됨.
        # return Response(template_name='blog/board.html')  # 됨. 근데 redirect 랑 둘 중에 뭘 써야할까


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

