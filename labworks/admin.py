from django.contrib import admin
from .models import LabWork


@admin.register(LabWork)
class LabWorkAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
