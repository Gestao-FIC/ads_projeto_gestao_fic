from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed

class AuthService:
    @staticmethod
    def authenticate_user(username, password):
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise AuthenticationFailed("Credenciais inválidas ou usuário inativo.")

        token, _ = Token.objects.get_or_create(user=user)
        return token
