from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class Survey(models.Model):

    name = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Question(models.Model):

    question_text = models.TextField()
    required = models.BooleanField(default=True)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name="question")

    TEXT = 'TEXT'
    RADIO = 'RADIO'
    SELECT_MULTIPLE = 'SELECT MULTIPLE'
    INTEGER = 'INTEGER'
    QUESTION_TYPE_CHOICES = (
        (TEXT, 'Text'),
        (RADIO, 'Radio'),
        (SELECT_MULTIPLE, 'Select multiple'),
        (INTEGER, 'Integer'),
    )
    question_type = models.CharField(
        max_length=50,
        choices=QUESTION_TYPE_CHOICES,
        default=TEXT,
    )

    def __str__(self):
        return self.question_text


class Choice(models.Model):

    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="choice")
    choice_text = models.CharField(max_length=200)

    def __str__(self):
        return self.choice_text


class Response(models.Model):
    """
    This provides a way to get a collection of questions and answers
    from a particular user for a particular survey.
    """
    response_id = models.CharField(max_length=150)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name="response")
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.response_id


class Answer(models.Model):

    answer_body = models.TextField(blank=True, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answer")
    response = models.ForeignKey(Response, on_delete=models.CASCADE, null=True,  related_name="answer")

    def __str__(self):
        return self.answer_body

    def save(self, *args, **kwargs):
        if Question.question_type == Question.INTEGER and not self.answer_body.isdigit():
            raise ValidationError(_('Value must be an integer'))
        super(Answer, self).save(*args, **kwargs)
