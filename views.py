from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Choice
# Create your views here.
def Index(request):
	qstobj = Question.objects.all()
	return render(request, 'Polls/Index.html', {'qst': qstobj})

def showchoices(request, questions_id):
	qstobj = Question.objects.get(pk = questions_id)
	return render(request, 'Polls/choices.html' , {'choice': qstobj})

def voted(request,questions_id):
	if request.method == 'POST':
		qstobj = Question.objects.get(pk = questions_id)
		try:
			choiceobj = get_object_or_404(Choice , pk = request.POST['choice'])
		except:
			return HttpResponse("Please select a valid option")
		else:
			choiceobj.votes +=1
			choiceobj.save()
			return render(request, 'Polls/choices.html', {'choice' : qstobj} )
	return render(request, 'Polls/choices.html')
