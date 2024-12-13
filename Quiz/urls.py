from django.urls import path
from . import views
urlpatterns = [
    #path('', views.index,name='index'),
    path('start-quiz/', views.start_quiz, name='start_quiz'),
    path('get-question/', views.get_question, name='get_question'),
    path('submit-answer/', views.submit_answer, name='submit_answer'),
    path('quiz-summary/', views.quiz_summary, name='quiz_summary'),
]
