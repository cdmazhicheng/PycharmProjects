from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Question
from django.template import loader

# def first_page(self):
#     return HttpResponse("测试...")

# def first_page(self):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     output = ';'.join([q.question_text for q in latest_question_list])
#     return HttpResponse(output)

# def index(self):
#     latest_question_list = Question.objects.all()
#     context = {
#         'latest_question_list': latest_question_list
#     }
#     mytemplate = loader.get_template('polls/index.html')
#     return HttpResponse(mytemplate.render(context, self))

# def detail(self, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(self, 'polls/detail.html', {'question': question})

def index(request):
    latest_question_list = Question.objects.all
    return render(request, 'polls/index.html', {'latest_question_list': latest_question_list})

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

