from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('index/', views.render_templates, name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('question_form/', views.CreateQuestion.as_view(), name='question_form'),
    path('choice_form/', views.CreateChoice.as_view(), name='choice_form'),
]
