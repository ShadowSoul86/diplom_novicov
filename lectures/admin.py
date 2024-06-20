from django.contrib import admin
from .models import Lecture


@admin.register(Lecture)
class LectureAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
