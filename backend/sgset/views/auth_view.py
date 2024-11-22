from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from ..serializers.auth_serializer import AuthSerializer
from ..services.auth_service import AuthService
from sgset.swagger.auth_response_schema import AuthViewSchema


class AuthView(APIView):
    """
    View para autenticação de usuários, gerando tokens de acesso.

    Este endpoint permite:
    - Autenticar usuários fornecendo credenciais (nome de usuário e senha).
    - Retornar um token de acesso se as credenciais forem válidas.
    """

    @swagger_auto_schema(
        **AuthViewSchema.post_schema
    )
    def post(self, request, *args, **kwargs):
        """
        Autenticar o usuário e retornar o token de acesso.

        Parâmetros:
        - request: Dados da solicitação contendo as credenciais do usuário (nome de usuário e senha).

        Retorna:
        - HTTP 200: Token gerado com sucesso.
        - HTTP 400: Requisição inválida, como falta de campos obrigatórios.
        - HTTP 401: Credenciais inválidas.

        Exemplo de Requisição:
        ```json
        {
            "username": "usuario123",
            "password": "senha_secreta"
        }
        ```

        Exemplo de Resposta (sucesso):
        ```json
        {
            "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
        }
        ```
        """
        serializer = AuthSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            try:
                token = AuthService.authenticate_user(username, password)
                return Response({'token': token.key}, status=status.HTTP_200_OK)
            except AuthenticationFailed as e:
                return Response({'error': str(e)}, status=status.HTTP_401_UNAUTHORIZED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
