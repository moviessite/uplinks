# Generated by Django 4.2 on 2023-06-09 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lastest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='latestcards',
            name='l_link',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
