# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .utils import paginate
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from .models import Question, Answer
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout


@require_GET
def main_page(request, *args, **kwargs):
    last_questions = Question.objects.new()
    page = paginate(request, last_questions)
    page.base_url = '/?page='
    return render(request, 'qa/index.html', {
        'questions': page.object_list,
        'page': page,
    })


def test(request):
    return HttpResponse(status=200)


def question(request):
    q = get_object_or_404(Question, id=id)
    a = q.answer_set.all()
    # a = Answer.objects.filter(question=question_id).order_by('-added_at')
    context = {'question': q, 'answers': a}
    return render(request, 'qa/question.html', context)


def popular(request):
    popular_questions = Question.objects.popular()
    page = paginate(request, popular_questions)
    page.base_url = '/popular/?page='
    return render(request, 'qa/index.html', {
        'questions': page.object_list,
        'page': page
    })
