from django.shortcuts import render

questions = [
    {
        'id' : idx,
        'title' : f'title {idx}',
        'text' : 'text text',
    } for idx in range(10)
]

def index(request):
    return render(request, 'index.html', {
        'questions' : questions,
    })

def ask(request):
    return render(request, 'ask.html', {})

def question_page(request):
    return render(request, 'question.html', {})

def tag_search(request):
    return render(request, 'tag_search.html', {
        'questions' : questions,
    })

def settings(request):
    return render(request, 'settings.html', {})

def login(request):
    return render(request, 'login.html', {})

def register(request):
    return render(request, 'signup.html', {})