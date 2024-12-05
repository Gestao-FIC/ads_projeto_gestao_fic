from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from ..serializers.course_serializer import CourseSerializer
from ..models.course import CourseModel
from ..swagger.course_response_schema import CourseResponseSchema


class CourseModelList(generics.ListCreateAPIView):
    """
    Endpoint para listar todos os cursos ou criar um novo curso.

    Este endpoint permite:
    - Recuperar uma lista de todos os cursos disponíveis no sistema.
    - Criar um novo curso fornecendo os dados necessários.
    """

    queryset = CourseModel.objects.all()
    serializer_class = CourseSerializer

    @swagger_auto_schema(
        operation_summary="Listar todos os cursos",
        operation_description="Recupera uma lista com todos os cursos disponíveis no sistema.",
        responses=CourseResponseSchema.get_course_list_response_schema(),
    )
    def get(self, request, *args, **kwargs):
        """
        Lista todos os cursos.

        Parâmetros:
        - request: Dados da solicitação.

        Retorna:
        - HTTP 200: Lista de cursos recuperada com sucesso.
        """
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Criar um novo curso",
        operation_description="Cria um novo curso fornecendo os dados necessários.",
        request_body=CourseSerializer,
        responses=CourseResponseSchema.get_course_list_response_schema(),
    )
    def post(self, request, *args, **kwargs):
        """
        Cria um novo curso.

        Parâmetros:
        - request: Dados da solicitação contendo as informações do novo curso.

        Retorna:
        - HTTP 201: Curso criado com sucesso.
        - HTTP 400: Erro de validação nos dados fornecidos.
        """
        return super().post(request, *args, **kwargs)


class CourseModelDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Endpoint para recuperar, atualizar ou deletar um curso específico.

    Este endpoint permite:
    - Recuperar os detalhes de um curso fornecendo seu UUID.
    - Atualizar as informações de um curso existente.
    - Deletar um curso específico.
    """

    queryset = CourseModel.objects.all()
    serializer_class = CourseSerializer

    @swagger_auto_schema(
        operation_summary="Recuperar um curso",
        operation_description="Recupera os detalhes de um curso específico fornecendo seu UUID.",
        responses=CourseResponseSchema.get_course_detail_response_schema(),
    )
    def get(self, request, *args, **kwargs):
        """
        Recupera os detalhes de um curso.

        Parâmetros:
        - request: Dados da solicitação.
        - kwargs: Argumentos nomeados contendo o UUID do curso.

        Retorna:
        - HTTP 200: Detalhes do curso recuperados com sucesso.
        - HTTP 404: Curso não encontrado.
        """
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Atualizar um curso",
        operation_description="Atualiza as informações de um curso existente fornecendo os novos dados.",
        request_body=CourseSerializer,
        responses=CourseResponseSchema.get_course_detail_response_schema(),
    )
    def put(self, request, *args, **kwargs):
        """
        Atualiza os detalhes de um curso.

        Parâmetros:
        - request: Dados da solicitação contendo os dados atualizados do curso.
        - kwargs: Argumentos nomeados contendo o UUID do curso.

        Retorna:
        - HTTP 200: Curso atualizado com sucesso.
        - HTTP 400: Erro de validação nos dados fornecidos.
        - HTTP 404: Curso não encontrado.
        """
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Deletar um curso",
        operation_description="Deleta um curso específico fornecendo seu UUID.",
        responses=CourseResponseSchema.get_course_detail_response_schema(),
    )
    def delete(self, request, *args, **kwargs):
        """
        Deleta um curso.

        Parâmetros:
        - request: Dados da solicitação.
        - kwargs: Argumentos nomeados contendo o UUID do curso.

        Retorna:
        - HTTP 204: Curso deletado com sucesso.
        - HTTP 404: Curso não encontrado.
        """
        return super().delete(request, *args, **kwargs)
