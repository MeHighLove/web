# Generated by Django 3.1.3 on 2020-11-17 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name='Опубликован'),
        ),
    ]
