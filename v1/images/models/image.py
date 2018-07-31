from django.db import models

from v1.utils.models.core import CoreModel


class Image(CoreModel):
    """
    Image model.

    All color images related to products
    """

    product_color = models.ForeignKey(
        "colors.ProductColor",
        on_delete=models.CASCADE,
        related_name="images",
    )

    path = models.TextField(unique=True, max_length=5000)

    class Meta:
        ordering = ["-id"]
        get_latest_by = "created"

    def __str__(self):
        return "{}".format(self.pk)
