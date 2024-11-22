from ..models import EventModel

class CalendarService:
    @staticmethod
    def create_event(data):
        
        return EventModel.objects.create(**data)

    @staticmethod
    def get_event(event_id):
        return EventModel.objects.filter(id=event_id).first()

    @staticmethod
    def update_event(event_id, data):
        event = EventModel.objects.filter(id=event_id).first()
        if event:
            for key, value in data.items():
                setattr(event, key, value)
            event.save()
        return event

    @staticmethod
    def delete_event(event_id):
        event = EventModel.objects.filter(id=event_id).first()
        if event:
            event.delete()
        return event

    @staticmethod
    def list_events():
        return EventModel.objects.all()
