# Generated by Django 3.1.3 on 2020-11-03 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moviedb', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='user',
        ),
    ]