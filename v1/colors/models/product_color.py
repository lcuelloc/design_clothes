from django.db import models

from v1.utils.models.core import CoreModel


class ProductColor(CoreModel):
    """
    Product Color.

    Product type and color combination
    """

    color = models.ForeignKey(
        "colors.Color",
        on_delete=models.CASCADE,
        related_name="product_colors",
    )

    product_type = models.ForeignKey(
        "products.ProductType",
        on_delete=models.CASCADE,
        related_name="product_colors",
    )

    class Meta:
        unique_together = ("color", "product_type")
        ordering = ["-id"]
        get_latest_by = "created"

    def __str__(self):
        return "{}".format(self.pk)
