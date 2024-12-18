from django.contrib import admin
from .models import Question, Submission

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'category', 'correct_option')
    list_filter = ('category',)
    search_fields = ('question_text',)

class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('user', 'question', 'user_answer', 'is_correct')
    list_filter = ('is_correct', 'user', 'question__category')
    search_fields = ('user__username', 'question__question_text')

admin.site.register(Question, QuestionAdmin)
admin.site.register(Submission, SubmissionAdmin)
