from django.urls import path
from django.views.generic import TemplateView
# from .views import UserApiView
from .views import Login, Logout, SignUp

urlpatterns = [
    path('api/login/', Login.as_view(), name='api/login'),
    path('api/signup/', SignUp.as_view(), name='api/signup'),
    path('api/logout/', Logout.as_view(), name='api/logout'),
    path('login/', TemplateView.as_view(template_name="user/login.html"), name='login'),
    path('signup/', TemplateView.as_view(template_name="user/signup.html"), name='signup'),
]

