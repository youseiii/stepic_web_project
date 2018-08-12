from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question, Answer
from django.core.paginator import Paginator


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def main(request):
    questions = Question.objects.new()
    page = request.GET.get('page')
    paginator = Paginator(questions, 10)
    paginator.baseurl = '/?page='
    questions_p = paginator.get_page(page)
    return render(request, 'qa/list.html', {'page': questions_p})


def popular(request):
    questions = Question.objects.popular()
    page = request.GET.get('page')
    paginator = Paginator(questions, 10)
    paginator.baseurl = '/?page='
    questions_p = paginator.get_page(page)
    return render(request, 'qa/list.html', {'page': questions_p})


def question_details(request, id):
    q = get_object_or_404(Question, id=id)
    answers = Answer.objects.filter(question=q).order_by('-added_at')
    return render(request, 'qa/question.html', {'question': q, 'answer_list': answers})