from django.contrib import admin

from v1.locations.models.location import Location
from v1.utils.admin.mixins import ShowFieldsAdminMixin


@admin.register(Location)
class LocationAdmin(ShowFieldsAdminMixin, admin.ModelAdmin):
    pass
