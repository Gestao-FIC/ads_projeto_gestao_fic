from requests import Response
from sgset.repositories.GoalRepository import GoalRepository
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


from sgset.serializers.GoalSerializer import GoalSerializer

class GoalView(APIView):
    """
    API View for managing goals.
    """

    def get(self, request, goal_id=None):
        """
        Retrieve a single goal or all goals.
        """
        if goal_id:
            goal = GoalRepository.get_goal_by_id(goal_id)
            if goal:
                serializer = GoalSerializer(goal)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({"error": "Goal not found."}, status=status.HTTP_404_NOT_FOUND)
        
        goals = GoalRepository.get_all_goals()
        serializer = GoalSerializer(goals, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Create a new goal.
        """
        serializer = GoalSerializer(data=request.data)
        if serializer.is_valid():
            new_goal = GoalRepository.create_goal(serializer.validated_data)
            return Response(GoalSerializer(new_goal).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, goal_id):
        """
        Update an existing goal.
        """
        goal = GoalRepository.get_goal_by_id(goal_id)
        if not goal:
            return Response({"error": "Goal not found."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = GoalSerializer(goal, data=request.data, partial=True)
        if serializer.is_valid():
            updated_goal = GoalRepository.update_goal(goal_id, serializer.validated_data)
            return Response(GoalSerializer(updated_goal).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, goal_id):
        """
        Delete a goal.
        """
        result = GoalRepository.delete_goal(goal_id)
        if result:
            return Response({"message": "Goal deleted."}, status=status.HTTP_204_NO_CONTENT)
        return Response({"error": "Goal not found."}, status=status.HTTP_404_NOT_FOUND)
