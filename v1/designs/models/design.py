from django.db import models
from django.template.defaultfilters import slugify

from unidecode import unidecode

from v1.utils.models.core import CoreModel


class Design(CoreModel):
    """
    Design model.

    All clothes designs
    """

    category_design = models.ForeignKey(
        "designs.CategoryDesign",
        on_delete=models.CASCADE,
        related_name="designs",
    )

    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    img = models.TextField(max_length=5000)
    is_custom = models.BooleanField(default=False)
    height = models.FloatField()
    width = models.FloatField()

    class Meta:
        ordering = ["-id"]
        get_latest_by = "created"

    def __str__(self):
        return "{}".format(self.pk)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(unidecode(self.name))
        super(Design, self).save(*args, **kwargs)
