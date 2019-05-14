from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question
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
    response = "You are looking at the results of question %s."
    return HttpResponse(response % questionId)

def vote(request, questionId):
    return HttpResponse("You are voting on question %s." %questionId)

def index(request):
    latestQuetionList = Question.objects.order_by('pubDate')[:5]
    # template = loader.get_template('polls/index.html')
    context = {
        'latestQuestionList': latestQuetionList
    }
    # return  HttpResponse(template.render(context, request))
    return  render(request, 'polls/index.html', context)