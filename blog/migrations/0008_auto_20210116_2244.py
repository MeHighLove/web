# Generated by Django 3.1.5 on 2021-01-16 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20210116_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='nickname',
            field=models.CharField(default='', max_length=256, null=True, verbose_name='Nickname'),
        ),
    ]
