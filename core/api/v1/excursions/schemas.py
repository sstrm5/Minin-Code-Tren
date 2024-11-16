from datetime import datetime
from ninja import Schema


class ExcursionListOutSchema(Schema):
    id: int
    title: str
    description: str
    start_price: float
    picture: str
    is_visible: bool
    created_at: datetime
    updated_at: datetime | None = None

    def from_entity(entity) -> 'ExcursionListOutSchema':
        return ExcursionListOutSchema(
            id=entity.id,
            title=entity.title,
            description=entity.description,
            start_price=entity.start_price,
            picture=entity.picture,
            is_visible=entity.is_visible,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )
