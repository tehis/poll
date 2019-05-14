from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.template import loader


def detail(request, questionId):
    return HttpResponse("You are looking at question %s." %questionId)

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