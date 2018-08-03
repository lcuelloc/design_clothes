from django.contrib import admin

from v1.statics.models.static import Static
from v1.utils.admin.mixins import ShowFieldsAdminMixin


@admin.register(Static)
class StaticAdmin(ShowFieldsAdminMixin, admin.ModelAdmin):
    pass
