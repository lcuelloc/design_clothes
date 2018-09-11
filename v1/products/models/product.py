from django.db import models
from django.template.defaultfilters import slugify

from unidecode import unidecode

from v1.utils.models.core import CoreModel


class Product(CoreModel):
    """
    Product model.

    Base product
    """

    category = models.ForeignKey(
        "categories.Category",
        on_delete=models.CASCADE,
        related_name="products",
    )

    name = models.CharField(max_length=255)
    html_content = models.TextField(max_length=10000, null=True, blank=True)
    price = models.IntegerField()
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ["-id"]
        get_latest_by = "created"

    def __str__(self):
        return "{}".format(self.pk)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(unidecode(self.name))
        super(Product, self).save(*args, **kwargs)
