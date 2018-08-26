from django.contrib import admin

from v1.prints.models.print_type import PrintType
from v1.prints.models.print_product import PrintProduct
from v1.utils.admin.mixins import ShowFieldsAdminMixin


@admin.register(PrintType)
class PrintTypeAdmin(ShowFieldsAdminMixin, admin.ModelAdmin):
    pass


@admin.register(PrintProduct)
class PrintProductAdmin(ShowFieldsAdminMixin, admin.ModelAdmin):
    pass
