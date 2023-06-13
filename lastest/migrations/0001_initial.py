# Generated by Django 4.2 on 2023-06-08 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='latestCards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('l_photo', models.FileField(default=None, max_length=400, null=True, upload_to='cardmedia/')),
                ('l_title', models.CharField(max_length=100)),
                ('l_descript', models.CharField(max_length=1000)),
                ('l_update', models.CharField(max_length=50)),
            ],
        ),
    ]
