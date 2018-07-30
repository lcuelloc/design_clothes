from django.contrib import admin

from v1.products.models.product import Product
from v1.products.models.category_product import CategoryProduct
from v1.products.models.product_type import ProductType
from v1.utils.admin.mixins import ShowFieldsAdminMixin


@admin.register(Product)
class ProductAdmin(ShowFieldsAdminMixin, admin.ModelAdmin):
    pass


@admin.register(CategoryProduct)
class CategoryProductAdmin(ShowFieldsAdminMixin, admin.ModelAdmin):
    pass


@admin.register(ProductType)
class ProductTypeAdmin(ShowFieldsAdminMixin, admin.ModelAdmin):
    pass
