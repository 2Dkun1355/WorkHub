from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User, JobSeekerProfile, Skill

@admin.register(User)
class UserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'first_name', 'last_name', 'user_type', 'is_active',)
    list_filter = ('user_type', 'is_staff', 'is_active')
    search_fields = ('username', 'email', 'first_name', 'last_name', 'telegram', 'phone_number',)
    ordering = ('username',)

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Особиста інформація', {'fields': ('photo', 'first_name', 'last_name','phone_number', 'email', 'telegram', 'birth_date')}),
        ('Права доступу', {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_type')}),
        ('Дати', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {'fields': ('username', 'password1', 'password2', 'user_type')}),
        ('Права доступу', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )

@admin.register(JobSeekerProfile)
class JobSeekerProfileAdmin(admin.ModelAdmin):
    autocomplete_fields = ['skills']
    list_display = ('user', 'profile_title', 'year_experience', 'salary_expectations', 'hourly_rate', 'created_at')
    search_fields = ('user__username', 'profile_title')
    list_filter = ('year_experience', 'salary_expectations', 'hourly_rate')
    ordering = ('user__username',)

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)