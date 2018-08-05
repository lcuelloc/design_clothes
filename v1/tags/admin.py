from django.contrib import admin

from v1.tags.models.tag import Tag
from v1.tags.models.tag_design import TagDesign
from v1.utils.admin.mixins import ShowFieldsAdminMixin


@admin.register(Tag)
class TagAdmin(ShowFieldsAdminMixin, admin.ModelAdmin):
    pass


@admin.register(TagDesign)
class TagDesignAdmin(ShowFieldsAdminMixin, admin.ModelAdmin):
    pass
