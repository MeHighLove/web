# Generated by Django 3.1.5 on 2021-01-16 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_answer_profile_question_tag'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'verbose_name': 'Ответ', 'verbose_name_plural': 'Ответы'},
        ),
        migrations.AlterField(
            model_name='tag',
            name='tg',
            field=models.CharField(max_length=256, unique=True, verbose_name='Тег'),
        ),
    ]
