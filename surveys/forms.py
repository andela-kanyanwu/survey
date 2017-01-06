from django.forms import formset_factory, ModelForm

from .models import Answer


class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['answer_body']

AnswerFormSet = formset_factory(AnswerForm)
