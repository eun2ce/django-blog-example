from django.db import models

from conduit.apps.core.models import TimestampedModel

class History(models.Model):
    slug = models.SlugField(db_index=True, max_length=255)
    title = models.CharField(db_index=True, max_length=255)

    description = models.TextField()
    body = models.TextField()

    author = models.CharField(max_length=255)

    tags = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (("slug", "updated_at"),)

    def __str__(self):
        return self.title


class Tag(TimestampedModel):
    tag = models.CharField(max_length=255)
    slug = models.SlugField(db_index=True, unique=True)

    def __str__(self):
        return self.tag
