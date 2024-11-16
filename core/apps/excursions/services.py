from core.apps.excursions.entities import Excursion as ExcursionEntity
from core.apps.excursions.models import Excursion


class ORMExcursionsService:
    def get_excursion_list(self):
        items = Excursion.objects.filter(
            is_visible=True).order_by('-created_at')
        return [item.to_entity() for item in items]
