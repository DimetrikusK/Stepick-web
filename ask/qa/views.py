# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from .models import Question, Answer
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .forms import AnswerForm


@require_GET
def main_page(request, *args, **kwargs):
    question_list = Question.objects.order_by('-id')
    paginator, page, limit = paginate(request, question_list)
    context = {
        'questions': page,
        'paginator': paginator,
        'limit': limit,
    }
    return render(request, 'qa/index.html', context)


def test(request):
    return HttpResponse(status=200)


def question(request, question_id):
    q = get_object_or_404(Question, question_id=question_id)
    a = q.answer_set.all()
    # a = Answer.objects.filter(question=question_id).order_by('-added_at')
    # form = AnswerForm(initial={'question': question_id})
    context = {'question': q, 'answers': a}
    return render(request, 'qa/question.html', context)


@require_GET
def popular(request):
    question_list = Question.objects.order_by('-rating')
    paginator, page, limit = paginate(request, question_list)
    context = {
        'questions': page,
        'paginator': paginator,
        'limit': limit,
    }
    return render(request, 'qa/popular.html', context)


def paginate(request, lst):
    # get limit
    try:
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10

    # if limit is too high, normalize it
    if limit > 100:
        limit = 10

    paginator = Paginator(lst, limit)

    # get current page
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404

    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    return paginator, page, limit