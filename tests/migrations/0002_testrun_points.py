# Generated by Django 3.1.6 on 2021-07-16 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testrun',
            name='points',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
    ]
