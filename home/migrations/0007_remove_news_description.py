# Generated by Django 5.0 on 2024-11-25 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_news_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='description',
        ),
    ]
