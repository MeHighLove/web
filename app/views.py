from django.shortcuts import render

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

def index(request):
    return render(request, 'index.html', {
        'questions' : questions,
    })

def ask(request):
    return render(request, 'ask.html', {})

def tag_search(request):
    return render(request, 'tag_search.html', {
        'questions' : questions,
    })

def tag_search(request, tg):
    return render(request, 'tag_search.html', {
        'tag' : tg,
        'questions' : questions,
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