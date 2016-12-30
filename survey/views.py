from django.shortcuts import render
from django.views.generic import View

from .forms import AnswerForm


class HomeView(View):

    def get(self, request):
        form = AnswerForm
        context = {
            'form': form
        }
        return render(request, 'survey/home.html', context)
