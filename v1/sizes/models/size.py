from django.db import models

from v1.utils.models.core import CoreModel


class Size(CoreModel):
    """
    Size model.

    clothing size
    """

    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["-id"]
        get_latest_by = "created"

    def __str__(self):
        return "{}".format(self.pk)
