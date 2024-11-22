from drf_yasg import openapi

class AuthViewSchema:
    """
    Classe contendo as definições Swagger para a AuthView.
    """

    post_schema = {
        "operation_summary": "Autenticar usuário",
        "operation_description": "Autentica o usuário fornecendo as credenciais e retorna um token de acesso.",
        "request_body": openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["username", "password"],
            properties={
                "username": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="Nome de usuário para autenticação."
                ),
                "password": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="Senha correspondente ao usuário."
                )
            },
            description="Credenciais do usuário para autenticação."
        ),
        "responses": {
            200: openapi.Response(
                description="Token gerado com sucesso",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'token': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="Token de autenticação gerado após o login."
                        )
                    }
                )
            ),
            400: openapi.Response(
                description="Requisição inválida",
                examples={"application/json": {"username": ["Este campo é obrigatório."]}}
            ),
            401: openapi.Response(
                description="Credenciais inválidas",
                examples={"application/json": {"error": "Credenciais inválidas"}}
            ),
        }
    }
