from django.db import models
from core.apps.common.models import TimedBaseModel
from core.apps.events.entities import Event as EventEntity

# Create your models here.


class Event(TimedBaseModel):
    SEASON_CHOICES = [
        ('winter', 'Зима'),
        ('spring', 'Весна'),
        ('summer', 'Лето'),
        ('autumn', 'Осень'),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField()
    season = models.CharField(
        max_length=10,
        choices=SEASON_CHOICES,
        default='summer',
        verbose_name=('Сезон'),
    )
    picture = models.ImageField(
        upload_to='events/pictures',
        blank=True,
        null=True,
    )
    is_visible = models.BooleanField(default=True)

    def to_entity(self):
        return EventEntity(
            id=self.id,
            title=self.title,
            description=self.description,
            season=self.season,
            picture=self.picture.url if self.picture else None,
            is_visible=self.is_visible,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'

    def __str__(self) -> str:
        return self.title
