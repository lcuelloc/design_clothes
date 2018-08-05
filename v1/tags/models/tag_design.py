from django.db import models

from v1.utils.models.core import CoreModel


class TagDesign(CoreModel):
    """
    Tag Design model.

    Tags designs relationship
    """

    tag = models.ForeignKey(
        "tags.Tag",
        on_delete=models.CASCADE,
        related_name="tag_designs",
    )
    design = models.ForeignKey(
        "designs.Design",
        on_delete=models.CASCADE,
        related_name="tag_designs"
    )

    class Meta:
        unique_together = ("tag", "design")
        ordering = ["-id"]
        get_latest_by = "created"

    def __str__(self):
        return "{}".format(self.pk)
