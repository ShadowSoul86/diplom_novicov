from django.contrib import admin
from .models import Test, Question, Answer, TestResult


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'test')
    inlines = [AnswerInline]


class TestAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'slug')
    readonly_fields = ('slug',)


class TestResultAdmin(admin.ModelAdmin):
    list_display = ('name', 'test', 'score', 'date_taken')


admin.site.register(Test, TestAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(TestResult, TestResultAdmin)
