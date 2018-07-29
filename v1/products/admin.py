from django.contrib import admin

from v1.products.models.product import Product
from v1.utils.admin.mixins import ShowFieldsAdminMixin


@admin.register(Product)
class ProductAdmin(ShowFieldsAdminMixin, admin.ModelAdmin):
    pass
