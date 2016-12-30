from django.shortcuts import render
from django.views.generic import View, ListView

from .forms import AnswerForm
from .models import Question, Choice, Survey


class HomeView(ListView):
    template_name = 'surveys/home.html'
    context_object_name = 'survey_list'

    def get_queryset(self):
        return Survey.objects.all()


class SurveyView(View):

    def get(self, request,  *args, **kwargs):
        survey_pk = kwargs.get('pk')
        answer_form = AnswerForm

        questions = Question.objects.filter(survey=survey_pk)

        context = {
            'answer_form': answer_form,
            'questions': questions
        }
        return render(request, 'surveys/survey.html', context)
