from django.contrib import admin

from v1.colors.models.color import Color
from v1.utils.admin.mixins import ShowFieldsAdminMixin


@admin.register(Color)
class ColorAdmin(ShowFieldsAdminMixin, admin.ModelAdmin):
    pass
