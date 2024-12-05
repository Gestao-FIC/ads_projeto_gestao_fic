from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from sgset.serializers.EventSerializer import EventSerializer
from ..services.GeneralCalendar import CalendarService

class EventListView(APIView):
    """Lida com listagem e criação de eventos."""
    def get(self, request):
        events = CalendarService.list_events()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            event = CalendarService.create_event(serializer.validated_data)
            return Response(EventSerializer(event).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EventDetailView(APIView):
    """Lida com leitura, atualização e exclusão de eventos específicos."""
    def get(self, request, pk):
        event = CalendarService.get_event(pk)
        if event:
            serializer = EventSerializer(event)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'error': 'Event not found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        event = CalendarService.get_event(pk)
        if not event:
            return Response({'error': 'Event not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = EventSerializer(event, data=request.data, partial=True)
        if serializer.is_valid():
            updated_event = CalendarService.update_event(pk, serializer.validated_data)
            return Response(EventSerializer(updated_event).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        event = CalendarService.delete_event(pk)
        if event:
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({'error': 'Event not found'}, status=status.HTTP_404_NOT_FOUND)
