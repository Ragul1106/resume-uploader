from django.contrib import admin
from django.utils.html import format_html
from .models import Resume

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'download_link')
    search_fields = ('name', 'email')

    def download_link(self, obj):
        if obj.file:
            return format_html('<a href="{}" class="btn btn-primary">Download Resume</a>', obj.file.url)
        return "No file uploaded"
    download_link.short_description = 'Download'
