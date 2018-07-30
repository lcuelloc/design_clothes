from django.db import models

from v1.utils.models.core import CoreModel


class CategoryProduct(CoreModel):
    """
    Category Product model.

    Category product relationship
    """

    category = models.ForeignKey(
        "categories.Category",
        on_delete=models.CASCADE,
        related_name="category_products",
    )
    product = models.ForeignKey(
        "products.Product",
        on_delete=models.CASCADE,
        related_name="category_products"
    )

    class Meta:
        unique_together = ("category", "product")
        ordering = ["-id"]
        get_latest_by = "created"

    def __str__(self):
        return "{}".format(self.pk)
