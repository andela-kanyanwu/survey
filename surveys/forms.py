from django import forms


class SurveyForm(forms.Form):

    def __init__(self, *args, **kwargs):
        survey = kwargs.pop('survey')
        super(SurveyForm, self).__init__(*args, **kwargs)

        for question in survey.questions.all():
            field_name = question.id
            if question.type == question.TEXT:
                field_type = forms.CharField(label=question.text,
                                             required=question.required,
                                             widget=forms.Textarea(attrs={'rows':4}))
            elif question.type == question.SELECT_ONE:
                choices = [(choice.id, choice.text) for choice in question.choices.all()]
                field_type = forms.ChoiceField(label=question.text,
                                               required=question.required,
                                               choices=choices,
                                               widget=forms.RadioSelect)
            elif question.type == question.SELECT_MULTIPLE:
                choices = [(choice.id, choice.text) for choice in question.choices.all()]
                field_type = forms.MultipleChoiceField(label=question.text,
                                                       required=question.required,
                                                       choices=choices,
                                                       widget=forms.CheckboxSelectMultiple)
            elif question.type == question.INTEGER:
                field_type = forms.IntegerField(label=question.text, required=question.required)

            self.fields.update({field_name: field_type})
