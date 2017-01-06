from django.shortcuts import render
from django.views.generic import View, ListView
from django.db.models import Count
from django.shortcuts import get_object_or_404

from .models import Question, Choice, Survey
from .forms import SurveyForm


class HomeView(ListView):
    template_name = 'surveys/home.html'
    context_object_name = 'survey_list'

    def get_queryset(self):
        return Survey.objects.all()


class SurveyView(View):

    def get(self, request,  *args, **kwargs):
        survey_pk = kwargs.get('pk')
        survey = get_object_or_404(Survey, pk=survey_pk)
        survey_form = SurveyForm(survey=survey)

        # survey = Survey.objects.get(id=survey_pk)

        context = {
            'survey_form': survey_form,
            'survey': survey
        }
        return render(request, 'surveys/survey.html', context)

    def post(self, request, *args, **kwargs):
        survey_pk = kwargs.get('pk')
        survey = get_object_or_404(Survey, pk=survey_pk)
        survey_form = SurveyForm(dict(request.POST), survey=survey)

        if survey_form.is_valid():
            print("yes")
            pass