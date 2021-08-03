from django.db import models


class EmailStatuses(models.TextChoices):
    DONE = 'D', 'done'
    FAILED = 'F', 'failed'
