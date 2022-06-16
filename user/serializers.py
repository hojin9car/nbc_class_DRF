from rest_framework import serializers
from .models import User as UserModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['username', 'password', 'email']


class LoginUserInfo(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['last_login', 'username', 'email', 'join_date', 'is_admin']
