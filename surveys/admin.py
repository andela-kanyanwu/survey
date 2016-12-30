from django.contrib import admin
from .models import Survey, Question, Answer, Choice
from nested_inline.admin import NestedStackedInline, NestedModelAdmin


class ChoiceInline(NestedStackedInline):
    model = Choice


class AnswerInline(NestedStackedInline):
    model = Answer
    extra = 1


class QuestionInline(NestedStackedInline):
    model = Question

    inlines = [ChoiceInline, AnswerInline]
    search_fields = ['question']


@admin.register(Survey)
class SurveyAdmin(NestedModelAdmin):
    inlines = [QuestionInline]