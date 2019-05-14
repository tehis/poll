from django.shortcuts import render
from django.http import HttpResponse
from .models import Question


def detail(request, questionId):
    return HttpResponse("You are looking at question %s." %questionId)

def results(request, questionId):
    response = "You are looking at the results of question %s."
    return HttpResponse(response % questionId)

def vote(request, questionId):
    return HttpResponse("You are voting on question %s." %questionId)

def index(request):
    latestQuetionList = Question.objects.order_by('ubDate')[:5]
    output = ', '.join([q.questionText for q in latestQuetionList])
    return  HttpResponse(output)
