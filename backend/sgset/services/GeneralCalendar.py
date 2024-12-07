from ..models import Event

class CalendarService:
    @staticmethod
    def create_event(data):
        
        return Event.objects.create(**data)

    @staticmethod
    def get_event(event_id):
        return Event.objects.filter(id=event_id).first()

    @staticmethod
    def update_event(event_id, data):
        event = Event.objects.filter(id=event_id).first()
        if event:
            for key, value in data.items():
                setattr(event, key, value)
            event.save()
        return event

    @staticmethod
    def delete_event(event_id):
        event = Event.objects.filter(id=event_id).first()
        if event:
            event.delete()
        return event

    @staticmethod
    def list_events():
        return Event.objects.all()
