from dataclasses import dataclass


@dataclass
class Event:
    id: int
    title: str
    description: str
    season: str
    picture: str | None
    is_visible: bool
    created_at: str
    updated_at: str
