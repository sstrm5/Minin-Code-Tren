from datetime import datetime
from ninja import Schema


class EventListOutSchema(Schema):
    id: int
    title: str
    description: str
    season: str
    picture: str
    is_visible: bool
    created_at: datetime
    updated_at: datetime | None = None

    def from_entity(entity) -> 'EventListOutSchema':
        return EventListOutSchema(
            id=entity.id,
            title=entity.title,
            description=entity.description,
            season=entity.season,
            picture=entity.picture,
            is_visible=entity.is_visible,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )
