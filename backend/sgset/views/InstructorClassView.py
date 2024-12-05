from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from sgset.serializers.InstructorClassSerializer import InstructorClassSerializer
from sgset.services.InstructorClassService import InstructorClassService
from uuid import UUID

class InstructorClassListView(APIView):
    """
    API View for listing and creating InstructorClasss.
    """

    def get(self, request, *args, **kwargs):
        """Handles GET requests to list all InstructorClasss."""
        InstructorClasss = InstructorClassService.list_instructorclass()
        serializer = InstructorClassSerializer(InstructorClasss, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """Handles POST requests to create a new InstructorClass."""
        serializer = InstructorClassSerializer(data=request.data)
        if serializer.is_valid():
            try:
                InstructorClass = InstructorClassService.create_instructorclass(serializer.validated_data)
                serializer = InstructorClassSerializer(InstructorClass)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except KeyError as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InstructorClassDetailView(APIView):
    """
    API View for retrieving, updating, and deleting a specific InstructorClass.
    """

    def get(self, request, InstructorClass_id: UUID, *args, **kwargs):
        """Handles GET requests to retrieve a specific InstructorClass."""
        try:
            InstructorClass = InstructorClassService.get_instructorclass(InstructorClass_id)
            serializer = InstructorClassSerializer(InstructorClass)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except NotFound as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, InstructorClass_id: UUID, *args, **kwargs):
        """Handles PUT requests to update a specific InstructorClass."""
        try:
            serializer = InstructorClassSerializer(data=request.data)
            if serializer.is_valid():
                InstructorClass = InstructorClassService.update_instructorclass(InstructorClass_id, serializer.validated_data)
                serializer = InstructorClassSerializer(InstructorClass)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except NotFound as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, InstructorClass_id: UUID, *args, **kwargs):
        """Handles DELETE requests to delete a specific InstructorClass."""
        try:
            InstructorClassService.delete_instructorClass(InstructorClass_id)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except NotFound as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
