from django.contrib import admin

from v1.sizes.models.size import Size
from v1.utils.admin.mixins import ShowFieldsAdminMixin


@admin.register(Size)
class SizeAdmin(ShowFieldsAdminMixin, admin.ModelAdmin):
    pass
