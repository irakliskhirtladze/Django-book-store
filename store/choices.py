from django.db.models import TextChoices


class CoverChoices(TextChoices):
    HARD = 'hard', 'Hard'
    SOFT = 'soft', 'Soft'
    SPECIAL = 'special', 'Special'

