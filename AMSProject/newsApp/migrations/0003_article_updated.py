# Generated by Django 3.2 on 2023-10-27 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsApp', '0002_article_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]