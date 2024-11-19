from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from sgset.serializers.EventSerializer import EventSerializer
from ..services.GeneralCalendar import CalendarService

class CalendarView(APIView):
    def get(self, request, event_id=None):
        if event_id:
            event = CalendarService.get_event(event_id)
            if event:
                serializer = EventSerializer(event)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({'error': 'Event not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            events = CalendarService.list_events()
            serializer = EventSerializer(events, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            event = CalendarService.create_event(serializer.validated_data)
            return Response(EventSerializer(event).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, event_id):
        event = CalendarService.get_event(event_id)
        if not event:
            return Response({'error': 'Event not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = EventSerializer(event, data=request.data, partial=True)
        if serializer.is_valid():
            updated_event = CalendarService.update_event(event_id, serializer.validated_data)
            return Response(EventSerializer(updated_event).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, event_id):
        event = CalendarService.delete_event(event_id)
        if event:
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({'error': 'Event not found'}, status=status.HTTP_404_NOT_FOUND)
