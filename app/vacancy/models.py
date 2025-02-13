from django.db import models
from users.models import JobEmployerProfile

class Vacancy(models.Model):
    user = models.ForeignKey(JobEmployerProfile, related_name='vacancy', on_delete=models.CASCADE, blank=True, null=True, verbose_name='Профіль роботодавця')
    title = models.CharField(max_length=100, blank=True, null=True,)

    class Meta:
        verbose_name = 'Вакансія'
        verbose_name_plural = 'Вакансії'


    def __str__(self):
        return self.title
