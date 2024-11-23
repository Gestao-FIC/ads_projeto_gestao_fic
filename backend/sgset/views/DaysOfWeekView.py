from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from sgset.serializers.DaysOfWeekSerializer import DaysOfWeekSerializer
from sgset.models import DayOfWeek
from uuid import UUID

class DayOfWeekListView(APIView):
    """
    API View for listing and creating days of the week.
    """

    def get(self, request, *args, **kwargs):
        """Handles GET requests to list all days of the week."""
        days_of_week = DayOfWeek.objects.all()
        serializer = DaysOfWeekSerializer(days_of_week, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """Handles POST requests to create a new day of the week."""
        serializer = DaysOfWeekSerializer(data=request.data)
        if serializer.is_valid():
            try:
                # Create the new DayOfWeek object
                day_of_week = serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except KeyError as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DayOfWeekDetailView(APIView):
    """
    API View for retrieving, updating, and deleting a specific day of the week.
    """

    def get(self, request, day_of_week_id: UUID, *args, **kwargs):
        """Handles GET requests to retrieve a specific day of the week."""
        try:
            day_of_week = DayOfWeek.objects.get(id=day_of_week_id)
            serializer = DaysOfWeekSerializer(day_of_week)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except DayOfWeek.DoesNotExist:
            raise NotFound("Day of the week not found")

    def put(self, request, day_of_week_id: UUID, *args, **kwargs):
        """Handles PUT requests to update a specific day of the week."""
        try:
            day_of_week = DayOfWeek.objects.get(id=day_of_week_id)
            serializer = DaysOfWeekSerializer(day_of_week, data=request.data)
            if serializer.is_valid():
                updated_day_of_week = serializer.save()
                return Response(DaysOfWeekSerializer(updated_day_of_week).data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except DayOfWeek.DoesNotExist:
            raise NotFound("Day of the week not found")

    def delete(self, request, day_of_week_id: UUID, *args, **kwargs):
        """Handles DELETE requests to delete a specific day of the week."""
        try:
            day_of_week = DayOfWeek.objects.get(id=day_of_week_id)
            day_of_week.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except DayOfWeek.DoesNotExist:
            raise NotFound("Day of the week not found")
