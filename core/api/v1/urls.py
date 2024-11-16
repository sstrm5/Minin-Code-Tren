from core.project import settings
from ninja import Router

# from core.api.v1.products.handlers import router as product_router
from core.api.v1.excursions.handlers import router as excursions_router
from core.api.v1.events.handlers import router as events_router

router = Router(tags=['v1'])
# router.add_router('products/', product_router)
# router.add_router('tests/', question_router)
# router.add_router('customers/', customer_router)
# router.add_router('guide/', guide_router)
router.add_router('excursions/', excursions_router)
router.add_router('events/', events_router)
