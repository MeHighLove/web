from django.shortcuts import render

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from blog.models import Article

questions = [
    {
        'id' : idx,
        'title' : f'title {idx}',
        'text' : f'text {idx}',
    } for idx in range(10)
]

answers = [
    {
        'id' : idx,
        'text' : f'text{idx}',
    } for idx in range(5)
]

def paginate(objects_list, request, per_page=10):
    paginator = Paginator(objects_list, per_page)
    page = request.GET.get('page', 1)
    page = paginator.get_page(page)
    return page

def index(request):
    lquestions = paginate(questions, request, 3)
    articles = Article.objects.published()
    return render(request, 'index.html', {
        'articles' : articles,
        'questions' : lquestions,
    })

def ask(request):
    return render(request, 'ask.html', {})

def tag_search(request, tg):
    lquestions = paginate(questions, request, 3)
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
    question = questions[pk]
    return render(request, 'question.html', {
        'question' : question,
        'answers' : answers,
    })