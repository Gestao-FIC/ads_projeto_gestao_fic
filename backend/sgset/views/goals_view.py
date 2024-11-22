from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from sgset.serializers.goals_serializer import GoalSerializer
from sgset.services.goals_service import GoalService
from uuid import UUID

class GoalListView(APIView):
    """
    API View for listing and creating goals.
    """

    def get(self, request, *args, **kwargs):
        """Handles GET requests to list all goals."""
        goals = GoalService.list_goals()
        serializer = GoalSerializer(goals, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

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

    def get(self, request, goal_id: UUID, *args, **kwargs):
        """Handles GET requests to retrieve a specific goal."""
        try:
            goal = GoalService.get_goal(goal_id)
            serializer = GoalSerializer(goal)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except NotFound as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)

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

    def delete(self, request, goal_id: UUID, *args, **kwargs):
        """Handles DELETE requests to delete a specific goal."""
        try:
            GoalService.delete_goal(goal_id)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except NotFound as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
