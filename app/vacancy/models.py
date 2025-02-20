from django.db import models
from django.utils.text import slugify
from common.models import JobFormat, Skill
from users.choices import ENGLISH_LEVELS_CHOICES
from users.models import JobEmployerProfile

class Vacancy(models.Model):
    profile = models.ForeignKey(JobEmployerProfile, related_name='vacancy', on_delete=models.CASCADE, blank=True, null=True, verbose_name='Профіль роботодавця')
    slug = models.SlugField(unique=True, blank=True, verbose_name='Індитифікатор')
    title = models.CharField(max_length=100, blank=True, null=True, verbose_name='Заголовок')
    description = models.TextField(blank=True, null=True, verbose_name='Опис')
    english_level = models.CharField(max_length=64, choices=ENGLISH_LEVELS_CHOICES, default='no_english', blank=True,
                                     null=True, verbose_name='Рівень англійської')
    year_experience = models.PositiveIntegerField(default=0, blank=True, null=True, verbose_name='Років досвіду')
    job_format = models.ForeignKey(JobFormat, related_name='vacancy', on_delete=models.CASCADE,null=True, blank=True, verbose_name='Формат роботи')
    skills = models.ManyToManyField(Skill, related_name='vacancy', blank=True, verbose_name='Навички')
    salary = models.PositiveIntegerField(blank=True, null=True, verbose_name='Зарплата')
    location = models.CharField(max_length=64, blank=True, null=True, verbose_name='Місто')
    is_active = models.BooleanField(default=True, verbose_name='Активна')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='Дата створення')
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name='Дата оновлення')

    class Meta:
        verbose_name = 'Вакансія'
        verbose_name_plural = 'Вакансії'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)