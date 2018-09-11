from django.db import models
from django.template.defaultfilters import slugify

from unidecode import unidecode

from v1.utils.models.core import CoreModel


class CategoryDesign(CoreModel):
    """
    Category design model.

    Category design entity to group designs
    """

    parent = models.ForeignKey(
        "self", null=True,
        on_delete=models.CASCADE,
        related_name="children",
    )

    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ["-id"]
        get_latest_by = "created"

    def __str__(self):
        return "{}".format(self.pk)

    def save(self, *args, **kwargs):

        if not self.id:
            self.slug = slugify(unidecode(self.name))
        super(CategoryDesign, self).save(*args, **kwargs)
