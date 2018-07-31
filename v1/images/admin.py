from django.contrib import admin

from v1.images.models.image import Image
from v1.utils.admin.mixins import ShowFieldsAdminMixin


@admin.register(Image)
class ImageAdmin(ShowFieldsAdminMixin, admin.ModelAdmin):
    pass
