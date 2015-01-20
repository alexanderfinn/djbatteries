from django.db import models


class DateTrackable(models.Model):
    """ Mixin for date tracking on the models """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    

    class Meta:
        abstract = True

