from django.contrib import admin
from .models import Option, Question, Test, Testrun, Answer


class AnswerAdmin(admin.ModelAdmin):
    model = Answer
    list_display = ['question', 'user_answer', 'user']


class QuestionAdmin(admin.ModelAdmin):
    model = Question
    list_display = ['text', 'right_option']


class TestAdmin(admin.ModelAdmin):
    model = Test
    list_display = ['id', 'title']


class TestrunAdmin(admin.ModelAdmin):
    model = Testrun
    list_display = ['id', 'test', 'points']


admin.site.register(Option)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Testrun, TestrunAdmin)
admin.site.register(Test, TestAdmin)
admin.site.register(Answer, AnswerAdmin)
