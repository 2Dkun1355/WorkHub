from django.contrib import admin
from vacancy.models import Vacancy

@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    autocomplete_fields = ['skills']
    list_display = ('title', 'profile__company_name', 'location', 'english_level', 'job_format', 'salary', 'is_active')
    list_filter = ('english_level', 'job_format', 'is_active')
    search_fields = ('title', 'profile__company_name', 'skills', 'location',)
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        (None, {'fields': ('profile',)}),
        ('Про вакансію', {'fields': ('title', 'description', 'skills', 'location', 'year_experience', 'english_level', 'job_format', 'salary', 'is_active')}),
        ('Дати', {'fields': ('created_at', 'updated_at')}),
    )

class VacancyInline(admin.StackedInline):
    model = Vacancy
    extra = 0
    autocomplete_fields = ['skills']
    readonly_fields = ('created_at', 'updated_at')
    classes = ('collapse',)

    fieldsets = (
        (None, {'fields': ('title',)}),
        ('Про вакансію', {'fields': ('description', 'skills', 'location', 'year_experience', 'english_level', 'job_format', 'salary' 'is_active')}),
        ('Дати', {'fields': ('created_at', 'updated_at')}),
    )
