from django.conf.urls import url, include

from rest_framework import routers

from .views import SurveyViewSet, QuestionViewSet, ChoiceViewSet, AnswerViewSet, ResponseViewSet


router = routers.DefaultRouter()
router.register(r'surveys', SurveyViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'choices', ChoiceViewSet)
router.register(r'answers', AnswerViewSet)
router.register(r'responses', ResponseViewSet)

# Wire up our API using automatic URL routing.
urlpatterns = [
    url(r'^', include(router.urls)),
]
