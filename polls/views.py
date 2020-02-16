from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse as HR
from .models import Question
from django.template import loader

def index(request) :
    question_list = Question.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('polls/index.html')
    context = {
        'question_list' : question_list,
    }
    return render(request, 'polls/index.html', context)

from django.shortcuts import get_object_or_404

def detail(request, question_id) :
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'polls/detail.html', {'question' : question})

def results(request, question_id) :
    response = "You're looking at the results of question {}".format(question_id)
    return HR(response)

def votes(request, question_id) :
    var_type = type(question_id)
    return HR("You're voting on question {}, type : {}".format(question_id, var_type))