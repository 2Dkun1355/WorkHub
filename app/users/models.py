from django.contrib.auth.models import AbstractUser
from django.db import models
from common.models import Skill, JobFormat
from .choices import USER_TYPE_CHOICES, ENGLISH_LEVELS_CHOICES

class User(AbstractUser):
    photo = models.ImageField(upload_to='users/', blank=True, null=True, verbose_name='Фото')
    user_type = models.CharField(max_length=20, blank=True, null=True, choices=USER_TYPE_CHOICES, verbose_name='Тип користувача')
    phone_number = models.CharField(max_length=10, unique=True, blank=True, null=True, verbose_name='Номер телефону')
    telegram = models.CharField(max_length=64, unique=True, blank=True, null=True, verbose_name='Телеграм')
    birth_date = models.DateField(default=None, null=True, blank=True, verbose_name='Дата народження')
    is_verified = models.BooleanField(default=False, verbose_name='Верефікація')

    def get_photo_url(self):
        if self.photo:
            return self.photo.url
        return '/static/images/user_default.jpg'

    @property
    def is_job_employer(self):
        return self.user_type == "job_employer"

    @property
    def is_job_seeker(self):
        return self.user_type == "job_seeker"

    @property
    def is_admin(self):
        return self.user_type == "staff"

class JobSeekerProfile(models.Model):
    user = models.OneToOneField(to='User', related_name='seeker_profile', on_delete=models.CASCADE, verbose_name='Користувач')
    title = models.CharField(max_length=128, blank=True, null=True, verbose_name='Посада')
    description = models.TextField(blank=True, null=True, verbose_name='Про себе')
    location = models.CharField(max_length=64, blank=True, null=True, verbose_name='Місто')
    skills = models.ManyToManyField(Skill, related_name='seeker_profile', blank=True, verbose_name='Навички')
    job_format = models.ManyToManyField(JobFormat, related_name='users', blank=True, verbose_name='Формат роботи')
    english_level = models.CharField(max_length=64, choices=ENGLISH_LEVELS_CHOICES,default='no_english', blank=True, null=True, verbose_name='Рівень англійської')
    year_experience = models.PositiveIntegerField(default=0, blank=True, null=True, verbose_name='Років досвіду')
    salary_expectations = models.PositiveIntegerField(default=0, blank=True, null=True, verbose_name='Зарплатні очікування')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='Дата створення')
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name='Дата оновлення')

    class Meta:
        verbose_name = 'Шукач роботи'
        verbose_name_plural = 'Шукачі роботи'

    def __str__(self):
        return self.user.username

class JobEmployerProfile(models.Model):
    user = models.OneToOneField(User, related_name='employer_profile', on_delete=models.CASCADE, verbose_name='Користувачі')
    logo = models.ImageField(upload_to='companies/', null=True, blank=True, verbose_name='Логотип')
    company_name = models.CharField(max_length=128, null=True, blank=True, verbose_name='Назва компанії')
    company_description = models.TextField(null=True, blank=True, verbose_name='Опис компанії')
    company_url = models.URLField(unique=True, null=True, blank=True, verbose_name='Опис компанії')
    location = models.CharField(max_length=64, null=True, blank=True, verbose_name='Місто')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='Дата створення')
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name='Дата оновлення')

    class Meta:
        verbose_name = 'Роботодавець'
        verbose_name_plural = 'Роботодавці'

    def __str__(self):
        if self.company_name:
            return self.company_name
        return self.user.username

    def get_logo_url(self):
        if self.logo:
            return self.logo.url
        return '/static/images/company_default.jpg'