from django.db import models
from .choices import SKILLS_CHOICES, JOB_FORMAT_CHOICES


class Skill(models.Model):
    name = models.CharField(max_length=64, choices=SKILLS_CHOICES, blank=True, null=True, unique=True, verbose_name='Навички')

    class Meta:
        verbose_name = 'Навичка'
        verbose_name_plural = 'Навички'

    def __str__(self):
        return self.name

class JobFormat(models.Model):
    name = models.CharField(max_length=64, choices=JOB_FORMAT_CHOICES, blank=True, null=True, unique=True,
                            verbose_name='Формат роботи')

    class Meta:
        verbose_name = 'Формат роботи'
        verbose_name_plural = 'Формати роботи'

    def __str__(self):
        return self.name