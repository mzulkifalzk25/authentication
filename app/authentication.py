from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from .models import UserProfile


class CustomAuthentication(BaseAuthentication):
    def authenticate(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return None

        try:
            user = UserProfile.objects.get(username=username, password=password)
        except UserProfile.DoesNotExist:
            raise AuthenticationFailed('Invalid credentials')

        return (user, None)
