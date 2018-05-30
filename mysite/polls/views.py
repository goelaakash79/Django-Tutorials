from django.shortcuts import render
from django.http import HttpResponse

from .models import Question

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = '<br><br> '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

def about(request):
    return HttpResponse("<h1>ABOUT US</h1>")

def detail(request, question_id):
    return HttpResponse("You afre looking at question %s." % question_id)

def results(request, question_id):
    response = "You are looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You are voting for question %s." % question_id)