from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib import auth

from blog.models import Question, Profile
from blog.models import Answer, Tag
from blog.forms import LoginForm, AskForm, RegisterForm, AnswerForm, SettingsForm, TagForm

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

@login_required
def settings(request):
    if request.method == 'GET':
        form = SettingsForm()
    else:
        form = SettingsForm(data=request.POST)
        if form.is_valid():
            us1 = User.objects.filter(email = form.cleaned_data.get('email'))
            us2 = User.objects.filter(username = form.cleaned_data.get('username'))
            if us1 and (us1.get().id != request.user.id):
                msg = u"This email has already been taken!"
                form._errors["email"] = form.error_class([msg])
                del form.cleaned_data["email"]
            else:
                if us2 and (us2.get().id != request.user.id):
                    msg = u"This username has already been taken!"
                    form._errors["username"] = form.error_class([msg])
                    del form.cleaned_data["username"]
                else:
                    request.user.username = form.cleaned_data.get('username')
                    request.user.email = form.cleaned_data.get('email')
                    avatar = form.cleaned_data.get('avatar')
                    if avatar:
                        request.user.profile.avatar = avatar
                    request.user.save()
                    request.user.profile.save()
                    return redirect('settings')

    ctx={'form': form}
    return render(request, 'settings.html', ctx)

def login(request):
    if request.method == 'GET':
        form = LoginForm()
        next_page = request.GET.get('next','')
        request.session['next_page'] = next_page
    else:
        form = LoginForm(data=request.POST)
        if form.is_valid():
            us1 = User.objects.filter(username = form.cleaned_data.get('username'))
            if us1:
                user = auth.authenticate(request, **form.cleaned_data)
                if user is not None:
                    auth.login(request, user)
                    next_page = request.session.pop('next_page')
                    if next_page:
                        return redirect(next_page)
                    else:
                        return redirect('home')
            else:
                msg = u"This username does not exist!"
                form._errors["username"] = form.error_class([msg])
                del form.cleaned_data["username"]

    ctx={'form': form}
    return render(request, 'login.html', ctx)

def register(request):
    if request.method == 'GET':
        form = RegisterForm()
    else:
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            us1 = User.objects.filter(email = form.cleaned_data.get('email'))
            if us1:
                msg = u"This email has already been taken!"
                form._errors["email"] = form.error_class([msg])
                del form.cleaned_data["email"]
            else:
                user = form.save()
                user.refresh_from_db()
                prof = Profile.objects.create(user = user)
                prof.save()
                return redirect('home')

    ctx={'form': form}
    return render(request, 'signup.html', ctx)

def question_page(request, pk):
    qqq = paginate(Answer.objects.q_find(pk), request, 3)
    question = Question.objects.id_find(pk)
    if request.method == 'GET':
        form = AnswerForm()
    else:
        form = AnswerForm(data=request.POST)
        if form.is_valid():
            if request.user.is_authenticated:
                answer = form.save(commit=False)
                answer.author = request.user.profile
                answer.question_id = pk
                answer.save()
                answer.question.answers = answer.question.answers + 1
                answer.question.save()
                return redirect(reverse('question', kwargs={'pk': pk}))
            else:
                return redirect('login')

    return render(request, 'question.html', {
        'question' : question,
        'elems' : qqq,
        'form' : form,
    })

def hot(request):
    qqq = paginate(Question.objects.hot(), request, 3)
    return render(request, 'hot.html', {
        'elems' : qqq,
    })

def logout(request):
    auth.logout(request)
    return redirect("/")

@login_required
def add_tag(request):
    if request.method == 'GET':
        form = TagForm()
    else:
        form = TagForm(data=request.POST)
        if form.is_valid():
            tag = Tag.objects.create(tg=form.cleaned_data.get('tag'))
            tag.save()
            return redirect('add_tag')
    ctx={'form': form}
    return render(request, 'add_tag.html', ctx)