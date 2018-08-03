from django.db import models

from v1.utils.models.core import CoreModel


class Static(CoreModel):
    """
    Static model.

    Basic static costs
    """

    stamped_light = models.IntegerField()
    print_dimension = models.IntegerField()
    paper_dimension = models.IntegerField()

    class Meta:
        ordering = ["-id"]
        get_latest_by = "created"

    def __str__(self):
        return "{}".format(self.pk)
