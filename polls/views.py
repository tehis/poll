from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.db.models import F
from django.views import generic

from .models import Question, Choice
from django.template import loader
from django.http import Http404


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latestQuestionList'

    def get_queryset(self):
        """ Return the last five published questions. """
        return Question.objects.order_by('pubDate')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

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
        # selectedchoice.votes += 1
        selectedchoice.votes = F('vote') + 1
        selectedchoice.save()
        return HttpResponseRedirect(reverse('polls:results',
                                             args = (question.id, )))
