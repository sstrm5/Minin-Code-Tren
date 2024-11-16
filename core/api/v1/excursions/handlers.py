from core.api.schemas import ApiResponse, ListResponse
from core.api.v1.excursions.schemas import ExcursionListOutSchema
from django.http import HttpRequest
from core.apps.excursions.services import ORMExcursionsService
from ninja import Router

router = Router(tags=['Excursions'])


@router.get('', response=ApiResponse)
def get_list_excursion(
    request: HttpRequest
):
    service = ORMExcursionsService()
    excursion_list = service.get_excursion_list()
    items = [ExcursionListOutSchema.from_entity(
        item) for item in excursion_list]
    return ApiResponse(data=ListResponse(items=items))
