from core.api.schemas import ApiResponse, ListResponse
from django.http import HttpRequest
from core.api.v1.events.schemas import EventListOutSchema
from core.apps.events.services import ORMEventsService
from ninja import Router

router = Router(tags=['Events'])


@router.get('', response=ApiResponse)
def get_list_events(
    request: HttpRequest
):
    service = ORMEventsService()
    events_list = service.get_events_list()
    items = [EventListOutSchema.from_entity(item) for item in events_list]
    return ApiResponse(data=ListResponse(items=items))
