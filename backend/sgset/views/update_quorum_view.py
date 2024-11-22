from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from ..models.course_class import CourseClassModel
from ..serializers.update_quorum_serializer import UpdateQuorumSerializer
from ..swagger.update_quorum_response_schema import UpdateQuorumResponseSchema


class UpdateCourseClassQuorum(generics.UpdateAPIView):
    """
    Endpoint para atualizar o quórum de uma turma específica.

    Este endpoint permite que o quórum de uma turma seja atualizado fornecendo
    o código da turma e o novo valor de quórum. Ele verifica a validade dos dados
    fornecidos antes de salvar a alteração no banco de dados.

    Métodos suportados:
    - PATCH: Atualiza apenas o campo de quórum de uma turma existente.
    """

    queryset = CourseClassModel.objects.all()
    serializer_class = UpdateQuorumSerializer

    @swagger_auto_schema(
        operation_summary="Atualizar o quórum de uma turma",
        operation_description="Atualiza apenas o quórum de uma turma específica fornecendo seu código e o novo valor de quórum.",
        request_body=UpdateQuorumSerializer,
        responses=UpdateQuorumResponseSchema.get_update_quorum_response_schema(),
    )
    def patch(self, request, *args, **kwargs):
        """
        Atualiza o quórum de uma turma.

        Parâmetros:
        - request: Dados fornecidos pelo cliente contendo o novo valor de quórum.
        - *args: Argumentos adicionais.
        - **kwargs: Argumentos nomeados adicionais.

        Retorna:
        - HTTP 200: Se o quórum foi atualizado com sucesso.
        - HTTP 400: Se os dados fornecidos forem inválidos.
        """
        course_class = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            new_quorum = serializer.validated_data["quorum"]
            course_class.quorum = new_quorum
            course_class.save()

            return Response(
                {"message": "Quórum atualizado com sucesso", "quorum": course_class.quorum},
                status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self):
        """
        Retorna o objeto CourseClassModel com base no código fornecido na URL.

        Este método verifica se existe uma turma com o código fornecido. 
        Caso não encontre, uma exceção `NotFound` é lançada.

        Retorna:
        - Instância do modelo CourseClassModel correspondente ao código.

        Lança:
        - NotFound: Se nenhuma turma com o código fornecido for encontrada.
        """
        try:
            return CourseClassModel.objects.get(code=self.kwargs['code'])
        except CourseClassModel.DoesNotExist:
            raise NotFound(f"Turma com o código '{self.kwargs['code']}' não encontrada.")
