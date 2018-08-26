from django.db import models
from django.template.defaultfilters import slugify

from unidecode import unidecode

from v1.utils.models.core import CoreModel


class PrintType(CoreModel):
    """
    PrintType model.

    Print types for clothes
    """

    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField(null=True, blank=True, max_length=5000)
    price = models.IntegerField()

    class Meta:
        ordering = ["-id"]
        get_latest_by = "created"

    def __str__(self):
        return "{}".format(self.pk)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(unidecode(self.name))
        super(PrintType, self).save(*args, **kwargs)
