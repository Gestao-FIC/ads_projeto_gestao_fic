from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from sgset.serializers.InstructorSerializer import InstructorSerializer
from sgset.services.InstructorService import InstructorService
from uuid import UUID

class InstructorListView(APIView):
    """
    API View for listing and creating Instructors.
    """

    def get(self, request, *args, **kwargs):
        """Handles GET requests to list all Instructors."""
        Instructors = InstructorService.list_instructors()
        serializer = InstructorSerializer(Instructors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """Handles POST requests to create a new Instructor."""
        serializer = InstructorSerializer(data=request.data)
        if serializer.is_valid():
            try:
                Instructor = InstructorService.create_instructor(serializer.validated_data)
                serializer = InstructorSerializer(Instructor)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except KeyError as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InstructorDetailView(APIView):
    """
    API View for retrieving, updating, and deleting a specific Instructor.
    """

    def get(self, request, Instructor_id: UUID, *args, **kwargs):
        """Handles GET requests to retrieve a specific Instructor."""
        try:
            Instructor = InstructorService.get_instructor(Instructor_id)
            serializer = InstructorSerializer(Instructor)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except NotFound as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, Instructor_id: UUID, *args, **kwargs):
        """Handles PUT requests to update a specific Instructor."""
        try:
            serializer = InstructorSerializer(data=request.data)
            if serializer.is_valid():
                Instructor = InstructorService.update_instructor(Instructor_id, serializer.validated_data)
                serializer = InstructorSerializer(Instructor)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except NotFound as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, Instructor_id: UUID, *args, **kwargs):
        """Handles DELETE requests to delete a specific Instructor."""
        try:
            InstructorService.delete_instructor(Instructor_id)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except NotFound as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
