from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Question, Choice
from django.template import loader
from django.http import Http404


def detail(request, questionId):
    # try:
        # question = Question.objects.get(pk=questionId)
    question = get_object_or_404(Question, pk=questionId)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exists")
    return render(request, 'polls/detail.html', {'question' : question})

def results(request, questionId):
    question = get_object_or_404(Question, pk = questionId)
    return render(request, 'polls/results.html', {'question' : question})

def vote(request, questionId) :
    question = get_object_or_404(Question, pk = questionId)
    try:
        selectedchoice = question.choice_set.get(pk = request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return  render(request, 'polls/detail.html', {
            'question' : question,
            'errorMessage' : "You didnt selected any choice!",
        })
    else:
        selectedchoice.votes += 1
        selectedchoice.save()
        return HttpResponseRedirect(reverse('polls:results',
                                             args = (question.id, )))


def index(request):
    latestQuetionList = Question.objects.order_by('pubDate')[:5]
    # template = loader.get_template('polls/index.html')
    context = {
        'latestQuestionList': latestQuetionList
    }
    # return  HttpResponse(template.render(context, request))
    return  render(request, 'polls/index.html', context)