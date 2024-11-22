from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from sgset.serializers.goals_serializer import GoalSerializer
from sgset.services.goals_service import GoalService
from sgset.swagger.goal_response_schema import GoalResponseSchema
from uuid import UUID
from drf_yasg.utils import swagger_auto_schema


class GoalListView(APIView):
    """
    API View for listing and creating goals.
    """

    @swagger_auto_schema(
        operation_summary="Listar todas as metas",
        operation_description="Recupera uma lista de todas as metas disponíveis no sistema.",
        responses=GoalResponseSchema.get_goal_list_response_schema(),
    )
    def get(self, request, *args, **kwargs):
        """Handles GET requests to list all goals."""
        goals = GoalService.list_goals()
        serializer = GoalSerializer(goals, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary="Criar uma nova meta",
        operation_description="Cria uma nova meta com os dados fornecidos.",
        request_body=GoalSerializer,
        responses=GoalResponseSchema.create_goal_response_schema(),
    )
    def post(self, request, *args, **kwargs):
        """Handles POST requests to create a new goal."""
        serializer = GoalSerializer(data=request.data)
        if serializer.is_valid():
            try:
                goal = GoalService.create_goal(serializer.validated_data)
                serializer = GoalSerializer(goal)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except KeyError as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GoalDetailView(APIView):
    """
    API View for retrieving, updating, and deleting a specific goal.
    """

    @swagger_auto_schema(
        operation_summary="Recuperar uma meta",
        operation_description="Recupera os detalhes de uma meta específica fornecendo seu UUID.",
        responses=GoalResponseSchema.get_goal_detail_response_schema(),
    )
    def get(self, request, goal_id: UUID, *args, **kwargs):
        """Handles GET requests to retrieve a specific goal."""
        try:
            goal = GoalService.get_goal(goal_id)
            serializer = GoalSerializer(goal)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except NotFound as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        operation_summary="Atualizar uma meta",
        operation_description="Atualiza os dados de uma meta específica fornecendo as novas informações.",
        request_body=GoalSerializer,
        responses=GoalResponseSchema.update_goal_response_schema(),
    )
    def put(self, request, goal_id: UUID, *args, **kwargs):
        """Handles PUT requests to update a specific goal."""
        try:
            serializer = GoalSerializer(data=request.data)
            if serializer.is_valid():
                goal = GoalService.update_goal(goal_id, serializer.validated_data)
                serializer = GoalSerializer(goal)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except NotFound as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        operation_summary="Deletar uma meta",
        operation_description="Deleta uma meta específica fornecendo seu UUID.",
        responses=GoalResponseSchema.delete_goal_response_schema(),
    )
    def delete(self, request, goal_id: UUID, *args, **kwargs):
        """Handles DELETE requests to delete a specific goal."""
        try:
            GoalService.delete_goal(goal_id)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except NotFound as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)