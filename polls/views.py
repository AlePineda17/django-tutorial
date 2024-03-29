from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from polls.models import Question, Choice


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html',
            {'question': question, 'error_message': "You didn't select a choice.", })
    else:
        selected_choice.votes += 1
        selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

class CreateQuestion(CreateView):
    model = Question
    fields = {
        'question_text',
        'pub_date',
    }
class CreateChoice(CreateView):
    model = Choice
    fields = {
        'question',
        'choice_text',
        'votes',
    }


def render_templates(request):
    return render(request, 'polls/index.html')



#class DeleteQuestion(DeleteView):
    #model = Question
    #template_name = 'polls/question_delete.html'

#class DeleteChoice(DeleteView):
    #template_name = 'polls/choice_delete.html'