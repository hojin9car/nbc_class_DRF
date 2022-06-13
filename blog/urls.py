from django.urls import path
from django.views.generic import TemplateView

from .views import ReadBlog, Write

urlpatterns = [
    path('blog/', ReadBlog.as_view(), name='blog'),
    path('api/write/', Write.as_view(), name='write'),
]

