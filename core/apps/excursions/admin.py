from django.contrib import admin
import nested_admin

from core.apps.excursions.models import Excursion

# Register your models here.


@admin.register(Excursion)
class ExcursionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'start_price', 'picture', 'created_at',
                    'updated_at', 'is_visible')
