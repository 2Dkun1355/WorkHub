from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User, JobSeekerProfile, JobEmployerProfile
from vacancy.admin import VacancyInline


@admin.register(User)
class UserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'first_name', 'last_name', 'user_type', 'is_active',)
    list_filter = ('user_type', 'is_staff', 'is_active')
    search_fields = ('username', 'email', 'first_name', 'last_name', 'telegram', 'phone_number',)
    ordering = ('username',)

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Особиста інформація', {'fields': ('photo', 'first_name', 'last_name', 'user_type', 'phone_number', 'email', 'telegram',)}),
        ('Права доступу', {'fields': ('is_verified', 'is_active', 'is_staff', 'is_superuser')}),
        ('Дати', {'fields': ('birth_date', 'last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {'fields': ('username', 'user_type', 'password1', 'password2')}),
        ('Права доступу', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )

@admin.register(JobSeekerProfile)
class JobSeekerAdmin(admin.ModelAdmin):
    autocomplete_fields = ['skills', 'job_format']
    list_display = ('user', 'title', 'location', 'year_experience', 'salary_expectations', 'created_at')
    search_fields = ('user__username', 'title', 'location')
    list_filter = ('year_experience',)
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('user__username',)

    fieldsets = (
        (None, {'fields': ('user',)}),
        ('Про кандидата',{'fields': ('title', 'description','skills','job_format', 'english_level', 'year_experience',)}),
        ('Заробітня плата', {'fields': ('salary_expectations',)}),
        ('Дати', {'fields': ('created_at', 'updated_at')}),
    )

@admin.register(JobEmployerProfile)
class JobEmployerAdmin(admin.ModelAdmin):
    list_display = ('user', 'company_name', 'location', 'created_at')
    search_fields = ('user__username', 'company_name', 'location')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('user__username',)

    fieldsets = (
        (None, {'fields': ('user',)}),
        ('Про компанію', {'fields': ('logo', 'company_name', 'company_description', 'company_url', 'location',)}),
        ('Дати', {'fields': ('created_at', 'updated_at')}),
    )

    inlines = [VacancyInline]


