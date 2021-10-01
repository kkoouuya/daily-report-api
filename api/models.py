from django.db import models
from markdownx.models import MarkdownxField
from model_utils.fields import StatusField
from model_utils import Choices
import uuid


class Daily(models.Model):
    STATUS = Choices(
        ('verygood', 'VeryGood'),
        ('good', 'Good'),
        ('normal', 'Normal'),
        ('bad', 'Bad'),
        ('wtf', 'WTF'),
    )
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    do = MarkdownxField(null=True, blank=True)
    study = MarkdownxField(null=True, blank=True)
    review = MarkdownxField(null=True, blank=True)
    score = StatusField()
    created_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(format(self.created_at, "%Y-%m-%d"))
