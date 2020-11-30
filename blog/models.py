from django.db import models
from django.utils import timezone

class Author(models.Model):
    name = models.CharField(max_length=256, verbose_name='Имя')
    birthday = models.DateField(verbose_name='Дата рождения')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Автор'
        verbose_name_plural='Авторы'

class ArticleManager(models.Manager):
    def published(self):
        return self.filter(is_published=True, date_published__lte=timezone.now())

class Article(models.Model):
    title = models.CharField(max_length=1024, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    is_published = models.BooleanField(default=False, verbose_name='Опубликован')
    date_published = models.DateTimeField(null=True, blank=True, verbose_name='Дата публикации')
    date_create = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    author = models.ForeignKey('Author', on_delete=models.CASCADE)

    objects = ArticleManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Статья'
        verbose_name_plural='Статьи'

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
    email = models.EmailField(max_length=256, default='', verbose_name='Email')
    nickname = models.CharField(max_length=256, default='', verbose_name='Nickname')
    avatar = models.ImageField(blank=True, default='static/img/113.jpg')

    objects = ProfileManager()

    def __str__(self):
        return self.nickname

    class Meta:
        verbose_name='Профиль'
        verbose_name_plural='Профили'

class QuestionManager(models.Manager):
    def tag_find(self, tag):
        return self.filter(tags__word__icontains=tag)
    def id_find(self, idx):
        return self.filter(id=idx)

class Question(models.Model):
    title = models.CharField(max_length=1024, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    date_create = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    tags = models.ManyToManyField('Tag')
    rating = models.IntegerField(default=0, verbose_name='Рейтинг')
    author = models.ForeignKey('Profile', on_delete=models.CASCADE)

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
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Текст')
    date_create = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    rating = models.IntegerField(default=0, verbose_name='Рейтинг')
    author = models.ForeignKey('Profile', on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False, verbose_name='Верный')

    objects = QuestionManager()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name='Ответ'
        verbose_name_plural='Ответы'