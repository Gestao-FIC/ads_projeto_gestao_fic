from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from ..serializers.course_class_serializer import CourseClassModelSerializer
from ..models.course_class import CourseClass
from ..swagger.course_class_response_schema import CourseClassResponseSchema


class CourseClassModelList(generics.ListCreateAPIView):
    """
    Endpoint para listar todas as turmas ou criar uma nova turma.

    Este endpoint permite:
    - Recuperar uma lista de todas as turmas disponíveis no sistema.
    - Criar uma nova turma fornecendo os dados necessários.
    """

    queryset = CourseClass.objects.all()
    serializer_class = CourseClassModelSerializer

    @swagger_auto_schema(
        operation_summary="Listar todas as turmas",
        operation_description="Recupera uma lista com todas as turmas disponíveis no sistema.",
        responses=CourseClassResponseSchema.get_course_list_response_schema(),
    )
    def get(self, request, *args, **kwargs):
        """
        Lista todas as turmas.

        Parâmetros:
        - request: Dados da solicitação.

        Retorna:
        - HTTP 200: Lista de turmas recuperada com sucesso.
        """
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Criar uma nova turma",
        operation_description="Cria uma nova turma fornecendo os dados necessários.",
        request_body=CourseClassModelSerializer,
        responses=CourseClassResponseSchema.get_course_list_response_schema(),
    )
    def post(self, request, *args, **kwargs):
        """
        Cria uma nova turma.

        Parâmetros:
        - request: Dados da solicitação contendo as informações da nova turma.

        Retorna:
        - HTTP 201: Turma criada com sucesso.
        - HTTP 400: Erro de validação nos dados fornecidos.
        """
        return super().post(request, *args, **kwargs)


class CourseClassModelDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Endpoint para recuperar, atualizar ou deletar uma turma específica.

    Este endpoint permite:
    - Recuperar os detalhes de uma turma fornecendo seu código.
    - Atualizar as informações de uma turma existente.
    - Deletar uma turma específica.
    """

    queryset = CourseClass.objects.all()
    serializer_class = CourseClassModelSerializer

    @swagger_auto_schema(
        operation_summary="Recuperar uma turma",
        operation_description="Recupera os detalhes de uma turma específica fornecendo seu código.",
        responses=CourseClassResponseSchema.get_course_detail_response_schema(),
    )
    def get(self, request, *args, **kwargs):
        """
        Recupera os detalhes de uma turma.

        Parâmetros:
        - request: Dados da solicitação.
        - kwargs: Argumentos nomeados contendo o código da turma.

        Retorna:
        - HTTP 200: Detalhes da turma recuperados com sucesso.
        - HTTP 404: Turma não encontrada.
        """
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Atualizar uma turma",
        operation_description="Atualiza as informações de uma turma existente fornecendo os novos dados.",
        request_body=CourseClassModelSerializer,
        responses=CourseClassResponseSchema.get_course_detail_response_schema(),
    )
    def put(self, request, *args, **kwargs):
        """
        Atualiza os detalhes de uma turma.

        Parâmetros:
        - request: Dados da solicitação contendo os dados atualizados da turma.
        - kwargs: Argumentos nomeados contendo o código da turma.

        Retorna:
        - HTTP 200: Turma atualizada com sucesso.
        - HTTP 400: Erro de validação nos dados fornecidos.
        - HTTP 404: Turma não encontrada.
        """
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Deletar uma turma",
        operation_description="Deleta uma turma específica fornecendo seu código.",
        responses=CourseClassResponseSchema.get_course_detail_response_schema(),
    )
    def delete(self, request, *args, **kwargs):
        """
        Deleta uma turma.

        Parâmetros:
        - request: Dados da solicitação.
        - kwargs: Argumentos nomeados contendo o código da turma.

        Retorna:
        - HTTP 204: Turma deletada com sucesso.
        - HTTP 404: Turma não encontrada.
        """
        return super().delete(request, *args, **kwargs)
