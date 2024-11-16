from core.apps.events.models import Event


class ORMEventsService:
    def get_events_list(self):
        items = Event.objects.filter(
            is_visible=True).order_by('-created_at')
        return [item.to_entity() for item in items]
