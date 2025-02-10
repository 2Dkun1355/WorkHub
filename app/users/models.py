from django.contrib.auth.models import AbstractUser
from django.db import models
from .choices import USER_TYPE_CHOICES, ENGLISH_LEVELS_CHOICES, SKILLS_CHOICES


class User(AbstractUser):
    photo = models.ImageField(upload_to='profiles/user/', blank=True, null=True, verbose_name='Фото')
    user_type = models.CharField(max_length=20, blank=True, null=True, choices=USER_TYPE_CHOICES, verbose_name='Тип користувача')
    phone_number = models.CharField(max_length=10, blank=True, null=True, verbose_name='Номер телефону')
    telegram = models.CharField(max_length=64, blank=True, null=True, verbose_name='Телеграм')
    birth_date = models.DateField(default=None, null=True, blank=True, verbose_name='Дата народження')

    def get_photo_url(self):
        if self.photo:
            return self.photo.url
        return '/static/images/default.png'

    @property
    def job_provider(self):
        return self.user_type == "job_provider"

    @property
    def is_job_seeker(self):
        return self.user_type == "job_seeker"

    @property
    def is_admin(self):
        return self.user_type == "staff"

class JobSeekerProfile(models.Model):
    user = models.OneToOneField(to='User', related_name='profile', blank=True, null=True, on_delete=models.CASCADE, verbose_name='Користувач')
    profile_title = models.CharField(max_length=128, blank=True, null=True, verbose_name='Посада')
    profile_info = models.TextField(blank=True, null=True, verbose_name='Про себе')
    location = models.CharField(max_length=64, blank=True, null=True, verbose_name='Місце перебування')
    skills = models.ManyToManyField(to='Skill', related_name='users', verbose_name='Навички')
    english_level = models.CharField(max_length=64, choices=ENGLISH_LEVELS_CHOICES,default='no_english', blank=True, null=True, verbose_name='Рівень англійської')
    year_experience = models.PositiveIntegerField(default=0, blank=True, null=True, verbose_name='Років досвіду')
    salary_expectations = models.PositiveIntegerField(default=0, blank=True, null=True, verbose_name='Зарплатні очікування')
    hourly_rate = models.PositiveIntegerField(default=0, blank=True, null=True, verbose_name='Погодина ставка')
    is_verified = models.BooleanField(default=False, verbose_name='Верефікація')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='Дата створення')
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name='Дата оновлення')

    class Meta:
        verbose_name = 'Профіль'
        verbose_name_plural = 'Профіль'

    def __str__(self):
        return self.user.username

class Skill(models.Model):
    name = models.CharField(max_length=64, choices=SKILLS_CHOICES, blank=True, null=True, unique=True, verbose_name='Навички')

    class Meta:
        verbose_name = 'Навичка'
        verbose_name_plural = 'Навички'

    def __str__(self):
        return self.name

# class JobProviderProfile(models.Model):