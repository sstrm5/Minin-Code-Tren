from django.db import models
from core.apps.common.models import TimedBaseModel
from core.apps.excursions.entities import Excursion as ExcursionEntity

# Create your models here.


class Excursion(TimedBaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_price = models.DecimalField(max_digits=10, decimal_places=2)
    picture = models.ImageField(
        upload_to='excursions/pictures',
        blank=True,
        null=True,
    )
    is_visible = models.BooleanField(default=True)

    def to_entity(self):
        return ExcursionEntity(
            id=self.id,
            title=self.title,
            description=self.description,
            start_price=self.start_price,
            picture=self.picture.url if self.picture else None,
            is_visible=self.is_visible,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )

    class Meta:
        verbose_name = 'Экскурсия'
        verbose_name_plural = 'Экскурсии'

    def __str__(self) -> str:
        return self.title
