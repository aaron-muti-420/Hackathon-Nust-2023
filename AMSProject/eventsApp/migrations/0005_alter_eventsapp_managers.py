# Generated by Django 3.2 on 2023-10-28 02:38

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('eventsApp', '0004_auto_20231028_0221'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='eventsapp',
            managers=[
                ('publishedEvents', django.db.models.manager.Manager()),
            ],
        ),
    ]