# Generated by Django 2.2.28 on 2025-02-06 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0004_page_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='slug',
        ),
    ]
