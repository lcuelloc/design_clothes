from django.db import models
from django.utils.translation import ugettext_lazy as _


class CoreModel(models.Model):
    """
    Core models for all database models
    """

    created = models.DateTimeField(
         _('created'), auto_now_add=True, null=True, db_index=True)
    updated = models.DateTimeField(
         _('updated'), auto_now=True, null=True, db_index=True)

    def __rep__(self):
        return '<{}:{} {}>'.format(self.__class__.__name__, self.pk, str(self))

    class Meta:
        abstract = True
