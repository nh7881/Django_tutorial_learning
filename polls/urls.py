from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    # ex: /polls/
    path('', views.index, name = 'index'),
    # ex : /polls/5
    path('<int:question_id>/', views.detail, name = 'detail'),
    # ex : /polls/5/results/
    path('<str:question_id>/results/', views.results, name = 'result'),
    # ex : /polls/5/votes/
    path('<int:question_id>/votes/', views.votes, name = 'votes'),
]
