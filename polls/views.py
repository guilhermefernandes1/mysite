from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Question, Choice


def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]

	template = 'polls/index.html'
	context = {
		'latest_question_list': latest_question_list,
	}
	return render(request, template, context)


def detail(request, question_id):
	#try:
	#	question = Question.objects.get(pk=question_id)
	#except Question.DoesNotExist:
	#	raise Http404("Question does not exist")
	
	template = 'polls/detail.html'
	question = get_object_or_404(Question, pk=question_id)
	context = {
		'question': question
	}	
	
	return render(request, template, context)
		


def results(request, question_id):
	response = "You're looking at the results of question %s."
	return HttpResponse(response % question_id)


def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'polls/detail.html', {'question': question, 'error_message': "You didn't select a choice.",})
	
	else: 
		selected_choice.votes += 1
		selected_choice.save()
		
		return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))		
