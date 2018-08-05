from django.contrib import admin

from v1.designs.models.category_design import CategoryDesign
from v1.utils.admin.mixins import ShowFieldsAdminMixin


@admin.register(CategoryDesign)
class CategoryDesginAdmin(ShowFieldsAdminMixin, admin.ModelAdmin):
    pass
