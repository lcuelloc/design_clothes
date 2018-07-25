from django.contrib import admin

from v1.categories.models.category import Category
from v1.utils.admin.mixins import ShowFieldsAdminMixin


@admin.register(Category)
class CategoryAdmin(ShowFieldsAdminMixin, admin.ModelAdmin):
    pass
