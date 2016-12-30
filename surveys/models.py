from django.db import models


class Survey(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Question(models.Model):
    question_text = models.TextField()
    required = models.BooleanField(default=True)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choice')

    def __str__(self):
        return self.choice_text

class Answer(models.Model):
    answer_text = models.CharField(max_length=200)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answer')

    def __str__(self):
        return self.answer_text
