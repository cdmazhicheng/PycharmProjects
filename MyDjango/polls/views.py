from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.template import loader
# Create your views here.

def index_one(request):
    result = []
    for i in range(8):
        result.append(i)
    return HttpResponse(result)

def index_two(request):
    return HttpResponse("Indextwo is Testing...")

def detail(request, question_id):
    return HttpResponse("you are looking at question %s" % question_id)

def index_three(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
