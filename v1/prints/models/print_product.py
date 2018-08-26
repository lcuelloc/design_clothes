from django.db import models

from v1.utils.models.core import CoreModel


class PrintProduct(CoreModel):
    """
    Print Product.

    Print Product combination
    """

    print_type = models.ForeignKey(
        "prints.PrintType",
        on_delete=models.CASCADE,
        related_name="print_products",
    )

    product_type = models.ForeignKey(
        "products.ProductType",
        on_delete=models.CASCADE,
        related_name="print_products",
    )

    class Meta:
        unique_together = ("print_type", "product_type")
        ordering = ["-id"]
        get_latest_by = "created"

    def __str__(self):
        return "{}".format(self.pk)
