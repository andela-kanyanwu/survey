from django.shortcuts import render
from django.views.generic import View, ListView
from django.db.models import Count

from .models import Question, Choice, Survey
from .forms import AnswerForm, AnswerFormSet


class HomeView(ListView):
    template_name = 'surveys/home.html'
    context_object_name = 'survey_list'

    def get_queryset(self):
        return Survey.objects.all()


class SurveyView(View):

    def get(self, request,  *args, **kwargs):
        survey_pk = kwargs.get('pk')

        survey = Survey.objects.get(id=survey_pk)

        context = {
            'survey': survey
        }
        return render(request, 'surveys/survey.html', context)

    def post(self, request, *args, **kwargs):
        survey_pk = kwargs.get('pk')
        answers = dict(request.POST)
        # get the number of questions in a survey
        # survey = Survey.objects.annotate(num_of_questions=Count('question')).get(id=survey_pk)
        # num_of_questions = survey.num_of_questions

        for key, value in answers:
            if key.startswith('answer'):
                # Get value of question id from the underscore delimiter in key
                question_id = key.split('_')[1]
                question = Question.objects.get(id=question_id)
                for answer in value:
                    pass
