from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.http import Http404
from django.urls import reverse
from django.views import generic
from django.utils import timezone


class IndexView(generic.ListView):
    template_name = 'apps/index.html'
    context_object_name = 'last'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'apps/detail.html'

    def get_queryset(self):
        return Question.objects.filter(pub_date=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'apps/results.html'
# Create your views here.
# def index(request, **kwargs):
#     last = Question.objects.order_by('-pub_date')[:5]
#     context = {'last': last}
#
#     #output = ','.join([q.question_text for q in last])
#     # response = HttpResponse('hello this is index %s' % kwargs)
#     #return HttpResponse(output)
#     return render(request, 'apps/index.html', context)
#
#
# def detail(request, question_id):
#     # return HttpResponse('this is look detail %s' % question_id)
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404('%s not exist' % question_id)
#     # return render(request, 'apps/detail.html', {'question': question})
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'apps/detail.html', {'question': question})
#
#
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'apps/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'apps/detail.html', {
            'question': question,
            'errMessage': 'you didn`t not choice'
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('apps:results', args=(question_id,)))
