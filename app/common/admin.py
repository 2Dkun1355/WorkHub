from django.contrib import admin
from common.models import Skill, JobFormat

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(JobFormat)
class JobFormatAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
