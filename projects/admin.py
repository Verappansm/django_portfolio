from django.contrib import admin
from .models import Project, Patent, Publication

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'tech_stack', 'github_link')

@admin.register(Patent)
class PatentAdmin(admin.ModelAdmin):
    list_display = ('title', 'google_link')

@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'google_link')

