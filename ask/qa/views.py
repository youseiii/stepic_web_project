from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question, Answer
from django.core.paginator import Paginator


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def main(request):
    questions = Question.objects.new()
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, limit)
    paginator.baseurl = '/?page='
    page = paginator.page(page)
    #return HttpResponse('main page')
    return render(request, 'qa/list.html', {'post_list': questions,
                                            'paginator': paginator,
                                            'page': page})


def popular(request):
    questions = Question.objects.popular()
    return render(request, 'qa/list.html', {'post_list': questions})


def question_details(request, id):
    q = get_object_or_404(Question, id=id)
    answers = Answer.objects.filter(question=q).order_by('-added_at')
    return render(request, 'qa/question.html', {'question': q, 'answer_list': answers})