from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib import auth

from blog.models import Question
from blog.models import Answer
from blog.forms import LoginForm, AskForm, RegisterForm

from django.contrib.auth.decorators import login_required

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

@login_required
def ask(request):
    if request.method == 'GET':
        form = AskForm()
    else:
        form = AskForm(data=request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user.profile
            question.save()
            return redirect(reverse('question', kwargs={'pk': question.pk}))
    ctx={'form': form}
    return render(request, 'ask.html', ctx)

def tag_search(request, tg):
    lquestions = paginate(Question.objects.tag_find(tg), request, 3)
    return render(request, 'tag_search.html', {
        'tag' : tg,
        'questions' : lquestions,
    })

def settings(request):
    return render(request, 'settings.html', {})

def login(request):
    if request.method == 'GET':
        form = LoginForm()
    else:
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = auth.authenticate(request, **form.cleaned_data)
            if user is not None:
                auth.login(request, user)
                return redirect("/") #нужны правильные редиректы

    ctx={'form': form}
    return render(request, 'login.html', ctx)

def register(request):
    if request.method == 'GET':
        form = RegisterForm()
    else:
        form = RegisterForm(data=request.POST)
        if form.is_valid():
                user = form.save()
                #user.profile.save()
                return redirect("/")

    ctx={'form': form}
    return render(request, 'signup.html', ctx)

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

def logout(request):
    auth.logout(request)
    return redirect("/")