from django.db import models

from v1.utils.models.core import CoreModel


class ProductSize(CoreModel):
    """
    Product Size.

    Product size and product color combination
    """

    size = models.ForeignKey(
        "sizes.Size",
        on_delete=models.CASCADE,
        related_name="product_sizes",
    )

    product_color = models.ForeignKey(
        "colors.ProductColor",
        on_delete=models.CASCADE,
        related_name="product_sizes",
    )

    stock = models.IntegerField(default=0)

    class Meta:
        unique_together = ("size", "product_color")
        ordering = ["-id"]
        get_latest_by = "created"

    def __str__(self):
        return "{}".format(self.pk)
