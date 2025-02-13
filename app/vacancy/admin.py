from django.contrib import admin
from vacancy.models import Vacancy

class VacancyInline(admin.TabularInline):
    model = Vacancy
    extra = 1
    fields = ('title',)