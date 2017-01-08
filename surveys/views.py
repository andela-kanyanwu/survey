from django.shortcuts import render, redirect
from django.views.generic import View, ListView, TemplateView
from django.shortcuts import get_object_or_404

from .models import Survey
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

        context = {
            'survey_form': survey_form,
            'survey': survey
        }
        return render(request, 'surveys/survey.html', context)

    def post(self, request, *args, **kwargs):
        survey_pk = kwargs.get('pk')
        survey = get_object_or_404(Survey, pk=survey_pk)
        survey_form = SurveyForm(request.POST, survey=survey)

        # get the nickname if any was passed in
        nickname = request.POST.get('nickname') if request.POST.get('nickname') else 'Anonymous'

        if survey_form.is_valid():
            survey_form.save(survey, nickname)
            # redirect to the response page
            return redirect('surveys:response')
        else:
            # re-render form with errors
            context = {
                'survey_form': survey_form,
                'survey': survey
            }
            return render(request, 'surveys/survey.html', context)


class ResponseView(TemplateView):
    template_name = 'surveys/response.html'
