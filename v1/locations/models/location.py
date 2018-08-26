from django.db import models

from v1.utils.models.core import CoreModel


class Location(CoreModel):
    """
    Location model.

    Locations of user
    """

    user = models.ForeignKey(
        "accounts.User", on_delete=models.CASCADE, related_name="locations"
    )

    country = models.CharField(max_length=255, default="Chile")
    region = models.CharField(max_length=255, default="RM")
    city = models.CharField(max_length=255)
    commune = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    secondary_address = models.CharField(max_length=255, null=True, blank=True)
    commentary = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        ordering = ["-id"]
        get_latest_by = "created"

    def __str__(self):
        return "{}".format(self.pk)
