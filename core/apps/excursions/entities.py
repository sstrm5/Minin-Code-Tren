from dataclasses import dataclass
from datetime import datetime


@dataclass
class Excursion:
    id: int
    title: str
    description: str
    start_price: float
    picture: str
    is_visible: bool
    created_at: datetime
    updated_at: datetime
