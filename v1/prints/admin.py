from django.contrib import admin

from v1.prints.models.print import Print
from v1.prints.models.print_product import PrintProduct
from v1.utils.admin.mixins import ShowFieldsAdminMixin


@admin.register(Print)
class PrintAdmin(ShowFieldsAdminMixin, admin.ModelAdmin):
    pass


@admin.register(PrintProduct)
class PrintProductAdmin(ShowFieldsAdminMixin, admin.ModelAdmin):
    pass
