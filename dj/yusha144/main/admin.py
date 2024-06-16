from django.contrib import admin
from .models import Course, Section, Chapter


# Регистрация моделей для панели администратора
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_by')
    search_fields = ('title', 'description', 'created_by__username')


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'course')
    search_fields = ('title', 'course__title')


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ('title', 'section')
    search_fields = ('title', 'section__title')
