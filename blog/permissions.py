from datetime import timedelta
from django.utils import timezone
from rest_framework.permissions import BasePermission


class SignUpMoreThanMinute(BasePermission):

    def has_permission(self, request, view):
        # return bool(request.user and request.user.join_date < (timezone.now() - timedelta(days=3)))
        return bool(request.user and request.user.join_date < (timezone.now() - timedelta(minutes=1)))



