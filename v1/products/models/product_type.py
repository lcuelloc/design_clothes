from django.db import models
from django.template.defaultfilters import slugify

from unidecode import unidecode

from v1.utils.models.core import CoreModel


class ProductType(CoreModel):
    """
    Product model.

    Base product
    """

    category_product = models.ForeignKey(
        "products.CategoryProduct",
        on_delete=models.CASCADE,
        related_name="product_types",
    )

    name = models.CharField(max_length=255)
    html_content = models.TextField(max_length=10000)
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
        super(ProductType, self).save(*args, **kwargs)
