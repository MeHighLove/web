from django.shortcuts import render

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from blog.models import Question
from blog.models import Answer

def paginate(objects_list, request, per_page=10):
    paginator = Paginator(objects_list, per_page)
    page = request.GET.get('page', 1)
    page = paginator.get_page(page)
    return page

def index(request):
    qqq = paginate(Question.objects.all().order_by('-date_create'), request, 3)
    return render(request, 'index.html', {
        'elems' : qqq,
    })

def ask(request):
    return render(request, 'ask.html', {})

def tag_search(request, tg):
    lquestions = paginate(Question.objects.tag_find(tg), request, 3)
    return render(request, 'tag_search.html', {
        'tag' : tg,
        'questions' : lquestions,
    })

def settings(request):
    return render(request, 'settings.html', {})

def login(request):
    return render(request, 'login.html', {})

def register(request):
    return render(request, 'signup.html', {})

def question_page(request, pk):
    qqq = paginate(Answer.objects.q_find(pk), request, 3)
    question = Question.objects.id_find(pk)
    return render(request, 'question.html', {
        'question' : question,
        'elems' : qqq,
    })

def hot(request):
    qqq = paginate(Question.objects.hot(), request, 3)
    return render(request, 'hot.html', {
        'elems' : qqq,
    })