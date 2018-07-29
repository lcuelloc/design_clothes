from django.db import models

from v1.utils.models.core import CoreModel
from v1.utils.models.upper_field import UpperCharField


class Size(CoreModel):
    """
    Size model.

    clothing size
    """

    name = UpperCharField(max_length=255, unique=True, uppercase=True)

    class Meta:
        ordering = ["-id"]
        get_latest_by = "created"

    def __str__(self):
        return "{}".format(self.pk)
