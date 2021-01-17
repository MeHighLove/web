from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Tag(models.Model):
    tg = models.CharField(unique=True, max_length=256, verbose_name='Тег')

    def __str__(self):
        return self.tg

    class Meta:
        verbose_name='Тег'
        verbose_name_plural='Теги'

class ProfileManager(models.Manager):
    def profile_find(self, profile_id):
        return self.filter(id=profile_id)

class Profile(models.Model):
    #email = models.EmailField(max_length=256, default='', verbose_name='Email')
    avatar = models.ImageField(blank=True, default='static/img/113.jpg')
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    objects = ProfileManager()

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name='Профиль'
        verbose_name_plural='Профили'

class QuestionManager(models.Manager):
    def tag_find(self, tag):
        return self.filter(tags=tag)
    def id_find(self, idx):
        return self.filter(id=idx).first
    def hot(self):
        return self.order_by('-rating')

class Question(models.Model):
    title = models.CharField(max_length=1024, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    date_create = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    tags = models.ManyToManyField('Tag')
    rating = models.IntegerField(default=0, verbose_name='Рейтинг')
    author = models.ForeignKey('Profile', verbose_name='Профиль', on_delete=models.CASCADE)
    answers = models.IntegerField(verbose_name='Число ответов', default=0)

    objects = QuestionManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Вопрос'
        verbose_name_plural='Вопросы'

class AnswerManager(models.Manager):
    def q_find(self, question_f):
        return self.filter(question=question_f)

class Answer(models.Model):
    question = models.ForeignKey('Question', verbose_name='Вопрос', on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Текст')
    date_create = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    rating = models.IntegerField(default=0, verbose_name='Рейтинг')
    author = models.ForeignKey('Profile', verbose_name='Профиль', on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False, verbose_name='Верный')

    objects = AnswerManager()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name='Ответ'
        verbose_name_plural='Ответы'