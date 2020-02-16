from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse as HR, HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice
from django.template import loader
from django.utils import timezone
# Create your views here.

def index(request) :
    question_list = Question.objects.filter(pub_date__lte = timezone.now()).order_by('-pub_date')[:5]
    #template = loader.get_template('polls/index.html')
    context = {
        'question_list' : question_list,
    }
    return render(request, 'polls/index.html', context)

def detail(request, question_id) :
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'polls/detail.html', {'question' : question})

def results(request, question_id) :
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'polls/results.html', {
        'question' : question,
    })

def votes(request, question_id) :
    question = get_object_or_404(Question, pk = question_id)
    try :
        selected_choice = question.choice_set.get(pk = request.POST['choice'])
    except (KeyError, Choice.DoesNotExist) :
        return render(request, 'polls/detail.html', {
            'question' : question,
            'error_message' : 'You did not select a choice.',
        })
    else :
        all_choice = question.choice_set.all()
        for choice in all_choice :
            if choice == selected_choice :
                selected_choice.votes += 1
            else :
                choice.votes -= 1
            choice.save()
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args = (question.id,)))