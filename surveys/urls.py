from django.conf.urls import url

from .views import HomeView, SurveyView


app_name = 'surveys'
urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^survey/(?P<pk>[0-9]+)', SurveyView.as_view(), name='survey')
]